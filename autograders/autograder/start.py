import docker
import logging
from os import environ
from queue import Queue
from grader import Worker
from grader import Bucket
from grader import Firebase


# configure logging
format = logging.Formatter('[%(asctime)s] (%(levelname)s) %(name)s: %(message)s')
rootLogger = logging.getLogger()
fileHandler = logging.FileHandler('autograder.log')
fileHandler.setLevel(logging.WARNING)
fileHandler.setFormatter(format)
rootLogger.addHandler(fileHandler)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(format)
rootLogger.addHandler(consoleHandler)
rootLogger.setLevel(logging.INFO)

# num workers
NUM_WORKERS = 4

# batch size
BATCH_SIZE = 10

# firebase db
firebase = Firebase(environ['FIREBASE_KEY'], environ['FIREBASE_DB'])

# AWS S3 bucket
bucket = Bucket(environ['S3_BUCKET'], environ['S3_BACKUP'])


# Sync Queue
Q = Queue()

# Docker client
client = docker.from_env()

# logger
logger = logging.getLogger("main")


# queue service
def main():
    # create workers
    logger.info("creating workers...")
    logger.info('test')
    pool = []
    for i in range(NUM_WORKERS):
        worker = Worker(Q, bucket, firebase, client)
        worker.start()
        pool.append(worker)
    # master worker
    logger.info('starting master worker')
    while True:
        try:
            # search for items in bucket
            logger.info('searching for pending files...')
            items = []
            for item in bucket.list():
                items.append(item.key)
                if len(items) == BATCH_SIZE:
                    break
            # continue searching ...
            if len(items) == 0:
                continue
            # enqueue items
            logger.info('grading: %s' % (','.join(items)))
            for item in items:
                Q.put(item)
            # wait for all tasks
            Q.join()
        except KeyboardInterrupt:
            break
    # wait for all task
    logger.info('waiting for all workers')
    Q.join()
    # signal exit
    logger.info('sending stop signal to workers')
    for i in range(NUM_WORKERS):
        Q.put(None)
    # wait for workers
    for w in pool:
        w.join()
    logger.info('all done :]')


if __name__ == '__main__':
    main()
