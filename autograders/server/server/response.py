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
    return jsonify({'status': 'error', 'msg': 'unexpected exception, internal server error'})


def missing_files(files):
    return jsonify({'status': 'error', 'msg': 'missing some files: ' + files})


def queue_error(url):
    return jsonify({
        'status': 'error',
        'msg': 'your last submit is still being reviewed (%s)...\n\nplease wait until it\'s over and try again' % url
    })


def ok(url):
    return jsonify({
        'status': 'ok',
        'msg': 'Your grade will be ready soon, you can check the status here %s' % url,
    })
