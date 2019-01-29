import os
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
                            # create temp dir
                            tmp = utils.tempdir()
                            # get lab autograder function
                            lab = labs.__dict__[repo]
                            # get lab expected files list
                            expected = labs.__dict__[repo + '_expected']
                            # unzip files
                            filename = os.path.join(tmp, 'lab.zip')
                            request.files['file'].save(filename)
                            utils.extract_to(filename, tmp)
                            utils.delete_file(filename)
                            # copy lab files
                            utils.copy_files(utils.join('files', repo), tmp)
                            # check expected files
                            not_found = utils.expected_files(expected, tmp)
                            if len(not_found) == 0:
                                # grade lab
                                result = lab(tmp, token)
                                grade, table = result[0:2]
                                # save result in db
                                utils.firebase().store_result(token, repo, grade)
                                # delete tmp dir
                                utils.delete_dir(tmp)
                                headers = ['Exercise', 'Grade', 'Message']
                                if len(result) == 2:
                                    # return result
                                    return response.result(grade, msg=utils.report(table, headers))
                                else:
                                    # return result + compilation errors
                                    report = utils.report(table, headers)
                                    if result[2].strip() != '':
                                        report += '\n\nMore Info:\n\n'
                                        report += result[2]
                                    return response.result(grade, msg=report)
                            # delte tmp dir
                            utils.delete_dir(tmp)
                            return response.missing_files(','.join(not_found))
                        return response.invalid_repo_name(repo)
                    return response.no_repo_name()
                return response.no_file()
            return response.invalid_token(token)
        return response.no_token()
    except Exception as e:
        print(e)
        return response.unexpected_exception()
