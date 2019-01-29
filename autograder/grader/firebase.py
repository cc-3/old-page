import firebase_admin
from datetime import datetime
from firebase_admin import db
from firebase_admin import auth
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
        try:
            return (db.reference('%s/%s' % (repo, token))).get()
        except Exception:
            return None

    # stores autograder result
    def store_result(self, token, repo, grade):
        timestamp = datetime.utcnow().isoformat()[0:19]
        ref = db.reference('%s/%s' % (repo, token))
        result = {'grade': grade, 'timestamp': timestamp}
        saved = ref.get()
        # save new result
        if saved is None:
            ref.set(result)
        # replace old result if the grade is better
        elif saved['grade'] < result['grade']:
            ref.set(result)
