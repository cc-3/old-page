import os
import sys
import zipfile
import requests

TITLE = '''   ___       __                        __
  / _ |__ __/ /____  ___ ________ ____/ /__ ____
 / __ / // / __/ _ \/ _ `/ __/ _ `/ _  / -_) __/
/_/ |_\_,_/\__/\___/\_, /_/  \_,_/\_,_/\__/_/
                   /___/

               Machine Structures
      Great Ideas in Computer Architecture'''


# repo name
NAME = ''

# debug grader
DEBUG = False
# debug URL
DEBUG_URL = 'http://localhost:5000/'


# get files to zip
def get_files():
    return []


# zip lab files
def zip_lab(token):
    print('zipping source files...')
    # create zip file
    filename = '%s-%s.zip' % (NAME, token)
    zip = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    try:
        # get all files to zip
        for f in get_files():
            zip.write(f)
        zip.close()
        return filename
    except FileNotFoundError:
        zip.close()
        print('')
        print('incomplete files, expected files: %s' % (','.join(get_files())))
        if os.path.exists(filename):
            os.remove(filename)
        sys.exit(1)
    except Exception:
        print('')
        print('an unexpected exception occurs while zipping lab files')
        if os.path.exists(filename):
            os.remove(filename)
        sys.exit(1)


# gets current server URL
def get_server():
    print('getting server url...')
    # debug ?
    if DEBUG:
        return DEBUG_URL
    # get from github
    return 'http://mooc.turing.galileo.edu'


# submit code
def submit(token):
    print(TITLE)
    print('')
    print('Lab: ' + NAME)
    print('')
    filename = zip_lab(token)
    try:
        info = {'repo': NAME, 'token': token}
        url = get_server()
        print('waiting for response...')
        print('')
        f = open(filename, 'rb')
        r = requests.post(url, files={'file': f}, data=info)
        f.close()
        if r.status_code == 200:
            json = r.json()
            print(json['msg'])
        else:
            msg = ' '.join(requests.status_codes._codes[500][0].split('_')).title()
            print('server return status code: %d (%s)' % (r.status_code, msg))
    except requests.exceptions.ConnectionError:
        print('connection to the server could not be established, try again...')
    except requests.exceptions.Timeout:
        print('request time exceed, try again...')
    except requests.exceptions.TooManyRedirects:
        print('server url is bad :( ...')
    except requests.exceptions.HTTPError:
        print('invalid request/response, try again...')
    except Exception:
        print('unexpected exception, try again...')
    finally:
        if os.path.exists('%s-%s.zip' % (NAME, token)):
            os.remove('%s-%s.zip' % (NAME, token))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        submit(sys.argv[1])
    elif len(sys.argv) == 3 and sys.argv[2] == '--debug':
        DEBUG = True
        submit(sys.argv[1])
    elif len(sys.argv) == 4 and sys.argv[2] == '--debug':
        DEBUG = True
        DEBUG_URL = sys.argv[3]
        submit(sys.argv[1])
    else:
        print('usage: ./submit <usertoken>')
