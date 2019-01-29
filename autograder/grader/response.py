from flask import jsonify


def no_token():
    return jsonify({'status': 'error', 'msg': 'token was not provided'})


def invalid_token(token):
    return jsonify({'status': 'error', 'msg': 'invalid token ' + token})


def no_file():
    return jsonify({'status': 'error', 'msg': 'code files not submitted'})


def no_repo_name():
    return jsonify({'status': 'error', 'msg': 'repo name was not provided'})


def invalid_repo_name(name):
    return jsonify({'status': 'error', 'msg': 'invalid repo name: ' + name})


def unexpected_exception():
    return jsonify({'status': 'error', 'msg': 'unexpected exception'})


def missing_files(files):
    return jsonify({'status': 'error', 'msg': 'missing some files: ' + files})


def result(grade, msg=''):
    return jsonify({'status': 'ok', 'grade': grade, 'msg': msg})
