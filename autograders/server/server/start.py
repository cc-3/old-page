import response
from os import remove
from os import environ
from flask import Flask
from flask import request
from flask_cors import CORS
from firebase import Firebase


# flask app
app = Flask('Autograders Server')
CORS(app)


# firebase db
firebase = Firebase(environ['FIREBASE_KEY'], environ['FIREBASE_DB'])


# valid repos
valid_repos = [
    'lab0_git',
    'lab1_c_gdb'
]


# dashboard url
url = 'https://cc-3.github.io/autograders/%s'


# gets db info
def in_queue(token, repo):
    dir = 'labs' if repo.startswith('lab') else 'projs'
    student_ref = '%s/%s/%s' % (dir, token, repo)
    queue_ref = 'queue/%s-%s' % (repo, token)
    result = False
    info = firebase.database().reference(student_ref).get()
    queue = firebase.database().reference(queue_ref).get()
    if info is not None and queue is not None:
        grading = info.get('grading')
        result = result or (grading and queue)
    return result


# saves status in firebase db
def save_to_db(token, repo):
    dir = 'labs' if repo.startswith('lab') else 'projs'
    student_ref = '%s/%s/%s' % (dir, token, repo)
    queue_ref = 'queue/%s-%s' % (repo, token)
    info = {'grading': True, 'timestamp': Firebase.get_timestamp()}
    firebase.database().reference(queue_ref).set(True)
    firebase.database().reference(student_ref).set(info)


# API method
@app.route('/', methods=['POST'], strict_slashes=False)
def grade():
    try:
        if 'token' in request.form:
            token = request.form['token']
            if firebase.validate_token(token):
                if 'file' in request.files:
                    if 'repo' in request.form:
                        repo = request.form['repo'].strip()
                        print(repo)
                        if (repo != '') and (repo in valid_repos):
                            route = 'labs' if repo.startswith('lab') else 'projects'
                            if not in_queue(token, repo):
                                # save zip fil
                                filename = '%s-%s.zip' % (repo, token)
                                request.files['file'].save(filename)
                                # TODO: save to bucket files
                                # remove local file
                                remove(filename)
                                # save info in db
                                save_to_db(token, repo)
                                # all ok
                                return response.ok(url % route)
                            # delte tmp dir
                            return response.queue_error(url % route)
                        return response.invalid_repo_name(repo)
                    return response.no_repo_name()
                return response.no_file()
            return response.invalid_token(token)
        return response.no_token()
    except Exception as e:
        # TODO: logs
        print(e)
        return response.unexpected_exception()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
