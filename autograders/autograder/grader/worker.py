import docker
import logging
import threading
import traceback
from . import utils


logger = logging.getLogger('worker')


# autograders worker
class Worker(threading.Thread):

    def __init__(self, queue, bucket, firebase, client):
        super(Worker, self).__init__()
        self.daemon = True
        self.queue = queue
        self.bucket = bucket
        self.client = client
        self.firebase = firebase

    def run(self):
        while True:
            # get next item from queue
            item = self.queue.get()
            # None is a stop signal
            if item is None:
                break
            try:
                logger.info('grading %s', item)
                # create a temp dir
                tmp = utils.tempdir()
                # download files from aws bucket
                filename = utils.join(tmp, item)
                logger.info('downloading file %s from AWS bucket', item)
                try:
                    self.bucket.download(item, filename)
                except Exception as e:
                    logger.error('could not download file %s (%s: %s)', str(item), type(e).__name__, str(e))
                    continue
                # extract files
                logger.info('extracting file %s to %s', item, tmp)
                utils.extract_to(filename, tmp, delete=True)
                # get repo name and token from item
                (repo, token) = item.split('-')
                token = token.rstrip('.zip')
                # copy files
                logger.info('copying base files from files/%s to %s', repo, tmp)
                utils.copy_files(utils.join('files', repo), tmp)
                utils.copy_file(utils.join('grader', 'utils.py'), tmp)
                # create docker container
                try:
                    logger.info('creating container with name %s', item)
                    container = self.client.containers.create(
                        image='autograders/tests',
                        name=item,
                        volumes={
                            tmp: {
                                'bind': '/autograder',
                                'mode': 'rw',
                            }
                        },
                        command="python3 check.py",
                        mem_limit='100m',
                        working_dir='/autograder'
                    )
                    logger.info('starting container %s', item)
                    container.start()
                    logger.info('wating for container %s', item)
                    container.wait()
                    logger.info('removing %s container from history', item)
                    container.remove(v=True, force=True)
                    logger.info('reading tests output json')
                    result = utils.read_json(utils.join(tmp, 'output.json'))
                    logger.info('deleting temp dir %s', tmp)
                    utils.delete_dir(tmp)
                    try:
                        logger.info('creating a backup...')
                        self.bucket.backup(item)
                    except Exception as e:
                        traceback.print_exc()
                        logger.warning('could not create a backup for %s (%s: %s)', item, type(e).__name__, str(e))
                    try:
                        logger.info('deleting file %s from queue', item)
                        self.bucket.delete(item)
                    except Exception as e:
                        logger.error('could not delete file %s from bucket (%s: %s)', item, type(e).__name__, str(e))
                        continue
                    logger.info('storing results in firebase db...')
                    dir = 'labs' if repo.startswith('lab') else 'projs'
                    self.firebase.database().reference('%s/%s/%s/grade' % (dir, token, repo)).set(result['grade'])
                    self.firebase.database().reference('%s/%s/%s/console' % (dir, token, repo)).set(result['output'])
                    self.firebase.database().reference('%s/%s/%s/grading' % (dir, token, repo)).set(False)
                    self.firebase.database().reference('queue/%s' % (item.strip('.zip'))).delete()
                    logger.info('reading results...')
                except docker.errors.ImageNotFound as e:
                    logger.error('could not create container (%s: %s)', type(e).__name__, str(e))
                except docker.errors.APIError as e:
                    logger.error('container returns an error (%s: %s)', type(e).__name__, str(e))
            except Exception as e:
                logger.error('unexpected exception occurs (%s: %s)', type(e).__name__, str(e))
            finally:
                self.queue.task_done()
