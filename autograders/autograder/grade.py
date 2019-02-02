import os
import sys
import yaml
import argparse
import numpy as np
from grader import utils
from grader import Bucket
from random import randint
from grader import Firebase
from tabulate import tabulate
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt


firebase = Firebase(os.environ['FIREBASE_KEY'], os.environ['FIREBASE_DB'])
bucket = Bucket(os.environ['S3_BUCKET'], os.environ['S3_BACKUP'])


# gets result from firebase
def get_result(token, repo):
    dir = 'labs' if repo.startswith('lab') else 'projs'
    return firebase.database().reference('%s/%s/%s' % (dir, token, repo)).get()


# gets firebase uid
def get_user_id(email):
    try:
        return firebase.auth().get_user_by_email(email).uid
    except Exception:
        return None


# loads students list
def load(students):
    with open(students, 'r') as f:
        return yaml.load(f)


# decodes timestamp
def decode_timestamp(timestamp):
    return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')


# gets assignment grade
def get_grade(token, repo, due_date, moss):
    result = get_result(token, repo)
    if result is None:
        return (0, 'No subio laboratorio al autograder')
    if moss:
        filename = '%s-%s' % (repo, token)
        bucket.download_backup(filename + '.zip', os.path.join('moss', filename + '.zip'))
        dir = os.path.join('moss', filename)
        if not os.path.exists(dir):
            os.system('mkdir %s' % dir)
        utils.extract_to(os.path.join('moss', filename + '.zip'), dir, delete=True)
    if 'timestamp' in result:
        sub_date = decode_timestamp(result['timestamp'])
        if sub_date > due_date:
            return (0, 'Su nota fue de %.2f pero entrego tarde' % result['grade'])
    return (result['grade'], '')


# compute statistics
def statistics(data, output, show=False):
    print('getting statistics...')
    grades = [e[3] for e in data]
    mean = sum(grades) / len(grades)

    def hex_value(color):
        color = color & 0xff
        first = hex(color & 0xf).lstrip('0x')
        first = '0' if first == '' else first
        second = hex((color & 0xf0) >> 4).lstrip('0x')
        second = '0' if second == '' else second
        return second + first

    def random_color():
        r = hex_value(randint(0, 255))
        r = hex_value(randint(0, 255))
        g = hex_value(randint(0, 255))
        b = hex_value(randint(0, 255))
        return '#' + r + g + b

    def hist(title, y):
        figure = plt.figure()
        ax = figure.add_subplot(111)
        y.sort()
        counter = Counter(y)
        frequencies = np.array(list(counter.values()))
        names = ['%.2f' % e for e in list(counter.keys())]
        x_coordinates = np.arange(len(counter))
        colors = [random_color() for c in names]
        ax.bar(x_coordinates, frequencies, align='center', color=colors)
        ax.xaxis.set_major_locator(plt.FixedLocator(x_coordinates))
        ax.xaxis.set_major_formatter(plt.FixedFormatter(names))
        plt.xticks(rotation='vertical')
        plt.ylabel('Frequency')
        plt.title(title.lower().capitalize())
        figure.tight_layout()
        plt.savefig('./results/%s-plot.png' % output, bbox_inches='tight')

    # plot history
    hist('Results (mean %.2f)' % mean, grades)


def grade(args):
    students = load(args.list)
    inpt = open(args.input, 'r', encoding='latin-1')
    out = open('./results/' + args.output + '-GES.csv', 'w', encoding='latin-1')
    due_date = decode_timestamp(args.due)
    start = False
    data = []
    print('getting results...')
    for line in inpt:
        if not start:
            if line.lower().strip().startswith('id'):
                start = True
            out.write(line)
        else:
            fmt = '%s,\'%s,%s,%.2f,%s,\n'
            line = line.strip()
            if line == '':
                continue
            line = line.split(',')
            id = line[0]
            id2 = line[1].strip('\'')
            title = line[2]
            uid = get_user_id(students[id2])
            if uid is None:
                data.append((id, id2, title, 0, 'No creo token y no subio laboratorio al autograder'))
                out.write(fmt % data[-1])
            else:
                data.append((id, id2, title, *get_grade(uid, args.repo, due_date, args.moss)))
                out.write(fmt % data[-1])
    inpt.close()
    out.close()
    statistics(data, args.output, show=args.show)
    print('printing results... (%s)' % args.output)
    print()
    results = tabulate(data, headers=['Id', 'Id2', 'Name', 'Grade', 'Comment'])
    print(results)
    with open('./results/%s-info.txt' % args.output, 'w') as f:
        f.write(results)
    print()
    if args.show:
        print('showing statistics...')
        plt.show()
    print()
    print(' => all done (%s)' % args.output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CC-3 Grades Script')
    parser.add_argument('--input', '-i', type=str, help='GES .csv input file', required=True)
    parser.add_argument('--list', '-l', type=str, help='students list .yml file', required=True)
    parser.add_argument('--repo', '-r', type=str, help='repository name, e.g lab0_git', required=True)
    parser.add_argument('--output', '-o', type=str, default='out', help='output name without extension')
    parser.add_argument('--due', '-d', type=str, help='assignment due date (UTC) (yyyy-mm-ddThh:mm:ss)', required=True)
    parser.add_argument('--moss', '-m', help='use moss', action='store_true')
    parser.add_argument('--clean', '-c', help='clean old results', action='store_true')
    parser.add_argument('--show', '-s', help='show histogram plot', action='store_true')
    args = parser.parse_args()
    # error handling
    if not os.path.exists(args.input):
        print('file %s does not exists')
        sys.exit(1)
    if not os.path.exists(args.list):
        print('file %s does not exists')
        sys.exit(1)
    if not (args.repo.startswith('lab') or args.repo.startswith('proj')):
        print('repo should start with lab or proj')
        sys.exit(1)
    try:
        decode_timestamp(args.due)
    except Exception:
        print('invalid due date %s, format expected: yyyy-mm-ddThh:mm:ss' % args.due)
        sys.exit(1)
    if args.clean:
        os.system('rm -rf moss')
        os.system('rm -rf results')
    if not os.path.exists('results'):
        os.system('mkdir results')
    if args.moss and not os.path.exists('moss'):
        os.system('mkdir moss')
    grade(args)
