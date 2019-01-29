import os
import boto3
from . import labs
from . import utils
from . import response
from flask import request


# Web App
APP = utils.get_app()

# Firebase app credentials
FIREBASE_KEY = os.environ.get('FIREBASE_KEY')

# Firebase app config
FIREBASE_CONFIG = {'databaseURL': os.environ.get('FIREBASE_DB')}

# Firebase App
FIREBASE = utils.create_firebase(FIREBASE_KEY, FIREBASE_CONFIG)


# API method
@APP.route('/', methods=['POST'], strict_slashes=False)
def grade():
    try:
        if 'token' in request.form:
            token = request.form['token']
            if utils.firebase().validate_token(token):
                if 'file' in request.files:
                    if 'repo' in request.form:
                        repo = request.form['repo'].strip()
                        if (repo != '') and (repo in labs.__dict__):
                            # unzip files
                            filename = '%s-%s.zip' % (repo, token)
                            request.files['file'].save(filename)
                            # save to bucker
                            utils.firebase().store_result(token, repo)
                            boto3.client('s3').upload_file(filename, 'autograders', filename)
                            utils.delete_file(filename)
                            return response.result(100, msg='OK')
                            # delte tmp dir
                        return response.invalid_repo_name(repo)
                    return response.no_repo_name()
                return response.no_file()
            return response.invalid_token(token)
        return response.no_token()
    except Exception as e:
        print(e)
        return response.unexpected_exception()
