import firebase_admin
from datetime import datetime
from firebase_admin import db
from firebase_admin import auth
from firebase_admin import credentials


class Firebase:

    # creates a firebase app
    def __init__(self, key, url):
        cred = credentials.Certificate(key)
        config = {'databaseURL': url}
        self.app = firebase_admin.initialize_app(cred, config)

    # validates user token
    def validate_token(self, token):
        try:
            auth.get_user(token, self.app)
            return True
        except ValueError:
            # None, empty or malformed token
            return False
        except auth.AuthError:
            # error occurs while retrieving the user
            # or if the specified user ID does not exist.
            return False

    # gets firebase database
    def database(self):
        return db

    # gets firebase auth
    def auth(self):
        return auth

    # gets UTC timestamp (ISO format)
    @staticmethod
    def get_timestamp():
        return datetime.utcnow().isoformat()[0:19]
