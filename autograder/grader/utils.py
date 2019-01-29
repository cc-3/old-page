import os
import re
import shutil
import zipfile
import tempfile
from glob import glob
from flask import Flask
from subprocess import run
from flask_cors import CORS
from tabulate import tabulate
from termcolor import colored
from .firebase import Firebase
from distutils.dir_util import copy_tree


# gets server app
def get_app(name='CC-3 Autograders'):
    app = Flask(name)
    CORS(app)
    return app


# creates firebase app
def create_firebase(key, config):
    return Firebase(key, config)


# gets firebase app
def firebase():
    from .settings import FIREBASE
    return FIREBASE


# extracs a zip file to a directory:
def extract_to(file, to):
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall(to)
    zip_ref.close()


# join paths
def join(*args):
    return os.path.join(*args)


# removes a directory
def delete_dir(dir):
    shutil.rmtree(dir)


# removes a file
def delete_file(f):
    os.remove(f)


# creates a temp directory
def tempdir(prefix='cc-3-temp', suffix=''):
    return tempfile.mkdtemp(prefix=prefix, suffix=suffix)


# copy files from one dir to another
def copy_files(dirfrom, dirto):
    if os.path.exists(dirfrom):
        for f in glob(os.path.join(dirfrom, '*')):
            if os.path.isdir(f):
                copy_tree(f, os.path.join(dirto, os.path.basename(f)))
            else:
                shutil.copy2(f, dirto)


# expected files
def expected_files(files, dir):
    dirfiles = os.listdir(dir)
    not_found = []
    for f in files:
        if f not in dirfiles:
            not_found.append(f)
    return not_found


# executes a shell command
def execute(cmd=[], shell=True, dir='.', timeout=5):
    return run(cmd, shell=shell, capture_output=True, cwd=dir, timeout=timeout)


# makes a target
def make(target='', dir='.'):
    return execute('make %s' % target, dir=dir)


# parses a form
def parse_form(f):
    f = open(f, 'r')
    p = re.compile(r'^[0-9]+( )*:[a-zA-Z0-9, ]+$')
    lookup = {}
    for line in f:
        line = line.strip()
        if p.search(line) is not None:
            vals = line.split(':')
            lookup[vals[0].strip()] = vals[1].strip()
    return lookup


# passed message
def passed(*args):
    if len(args) > 0:
        return colored('passed', 'green') + ': ' + args[0]
    return colored('passed', 'green')


# failed message
def failed(*args):
    if len(args) > 0:
        return colored('failed', 'red') + ': ' + args[0]
    return colored('failed', 'red')


# incomplete message
def incomplete(*args):
    if len(args) > 0:
        return colored('imcomplete', 'yellow') + ': ' + args[0]
    return colored('incomplete', 'yellow')


# creates a compilation error msg
def create_error(filename, msg):
    if msg != '':
        return '[%s]\n\n%s\n' % (filename, msg)
    return ''


# creates a pretty result report
def report(table, headers):
    headers = [colored(header, 'white', attrs=['bold']) for header in headers]
    return tabulate(table, headers=headers)
