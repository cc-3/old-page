import firebase_admin
from firebase_admin import db
from firebase_admin import auth
from .utils import get_timestamp
from firebase_admin import credentials
from firebase_admin.auth import get_user


class Firebase:

    # creates a firebase app
    def __init__(self, key, config):
        cred = credentials.Certificate(key)
        self.app = firebase_admin.initialize_app(cred, config)

    # get users
    def get_user_id(self, email):
        try:
            return auth.get_user_by_email(email).uid
        except Exception:
            return None

    # validates user token
    def validate_token(self, token):
        try:
            get_user(token, self.app)
            return True
        except Exception:
            return False

    # gets result
    def get_result(self, token, repo):
        dir = 'labs' if repo.startswith('lab') else 'projs'
        try:
            return (db.reference('%s/%s/%s' % (dir, token, repo))).get()
        except Exception:
            return None

    def database(self):
        return db

    def auth(self):
        return auth

    # stores autograder result
    def store_result(self, token, repo):
        dir = 'labs' if repo.startswith('lab') else 'projs'
        db.reference('%s/%s/%s' % (dir, token, repo))
        student = '%s/%s/%s' % (dir, token, repo)
        queue = 'queue/%s-%s' % (repo, token)
        info = {'grading': True, 'timestamp': get_timestamp()}
        db.reference(student).set(info)
        db.reference(queue).set(True)
