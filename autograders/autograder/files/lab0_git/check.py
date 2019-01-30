import utils


# checks exercise 3
def check_ex3():
    try:
        lookup = utils.parse_form('./ex3.txt')
        # grade questions if any
        frac = 40 / 6
        grade = 0
        msg = []
        # grade question 1
        q1 = lookup.get('1')
        if q1 is not None and len(q1.split(',')) == 5:
            q1 = q1.split(',')
            q1r = []
            success = True
            for num in q1:
                try:
                    q1r.append(int(num))
                except Exception:
                    msg.append('q1')
                    success = False
                    break
            if success:
                expected = [6, 9, 15, 9, 9]
                for a, e in zip(q1r, expected):
                    if a != e:
                        msg.append('q1')
                        success = False
                        break
                if success:
                    grade += frac
        else:
            msg.append('q1')
        # grade question 2
        q2 = lookup.get('2')
        if q2 is not None and len(q2.split(',')) == 5:
            q2 = q2.split(',')
            q2r = []
            success = True
            for num in q2:
                num = num.lower()
                try:
                    if num.startswith('0x'):
                        num = num[2:]
                    q2r.append(int(num, 16))
                except Exception:
                    msg.append('q2')
                    success = False
                    break
            if success:
                expected = [0x6, 0x9, 0xf, 0x9, 0x9]
                for a, e in zip(q1r, expected):
                    if a != e:
                        msg.append('q2')
                        success = False
                        break
                if success:
                    grade += frac
        else:
            msg.append('q2')
        # grade question 3
        q3 = lookup.get('3')
        if q3 is not None and q3.lower() == 'j':
            grade += frac
        else:
            msg.append('q3')
        # grade question 4
        q4 = lookup.get('4')
        if q4 is not None and q4.lower() == 'f':
            grade += frac
        else:
            msg.append('q4')
        # grade question 5
        q5 = lookup.get('5')
        try:
            q5 = q5.lower()
            if q5.startswith('0x'):
                q5 = q5[2:]
            if int(q5, 16) == 0x88f9f or int(q5) == 0x88e9f:
                grade += frac
        except Exception:
            msg.append('q5')
        # grade question 6
        q6 = lookup.get('6')
        if q6 is not None and q6.lower() in ['n', 'no', '0']:
            grade += frac
        else:
            msg.append('q6')
        # return results
        if len(msg) == 0:
            return (round(grade), utils.passed())
        elif len(msg) < 6:
            return (round(grade), utils.incomplete('missing: ' + ','.join(msg)))
        else:
            return (round(grade), utils.failed('all answers are wrong'))
    except Exception:
        return (0, utils.failed('unexpected exception'))


# checks exercise 4
def check_ex4():
    try:
        f = open('./ex4.txt', 'r')
        lines = f.read().strip()
        if len(lines) >= 0:
            line = lines.split(',')
            if len(line) == 10:
                envelopes = list(map(lambda x: x.strip(), line))
                answer = []
                for env in envelopes:
                    try:
                        answer.append(int(env))
                    except Exception:
                        return (0, utils.failed('invalid decimal: ' + env))
                if sum(answer) == 1000:
                    expected = [1, 2, 4, 8, 16, 32, 64, 128, 256, 489]
                    grade = 0
                    for a, e in zip(answer, sorted(expected)):
                        if a == e:
                            grade += 4
                    msg = {0: utils.failed(), 40: utils.passed()}
                    return (grade, msg.get(grade, utils.incomplete()))
                if sum(answer) < 1000:
                    return (0, utils.failed('ex4.txt sum < 1000'))
                return (0, utils.failed('ex4.txt sum > 1000'))
            return (0, utils.failed('ex4.txt invalid format'))
        return (0, utils.failed('ex4.txt is empty'))
    except Exception:
        return (0, utils.failed('unexpected exception'))


# lab 0 autograder
def lab0_git():
    not_found = utils.expected_files(['./hello.sh', './ex3.txt', './ex4.txt'])
    if len(not_found) == 0:
        ex2_result = ('2. git and Remotes', 20, utils.passed())
        ex3_result = ('3. Binary Alphabet', *check_ex3())
        ex4_result = ('4. 1000 $1 Bills', *check_ex4())
        grade = 0
        grade += ex2_result[1]
        grade += ex3_result[1]
        grade += ex4_result[1]
        grade = min(grade, 100)
        report = utils.report([ex2_result, ex3_result, ex4_result])
        utils.write_result(grade, report)
    else:
        utils.write_result(0, 'missing files: %s' % (','.join(not_found)))


if __name__ == '__main__':
    lab0_git()
