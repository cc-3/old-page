import utils
import resource
import subprocess
from random import randint

# 195 MiB of memory
BYTES = 195 * 1024 * 1024


# checks ex1.txt
def check_ex1():
    grade = 0
    lookup = utils.parse_form('./ex1/ex1.txt')
    wrong = []
    # question 1
    ans1 = lookup.get('1')
    if ans1 is not None and ans1.lower() == 'b':
        grade += 1
    else:
        wrong.append('q1')
    # question 2
    ans2 = lookup.get('2')
    if ans2 is not None and ans2.lower() == '34':
        grade += 1
    else:
        wrong.append('q2')
    # question 3
    ans3 = lookup.get('3')
    if ans3 is not None and ans3.lower() == 'c':
        grade += 1
    else:
        wrong.append('q3')
    # question 4
    ans4 = lookup.get('4')
    if ans4 is not None and (ans4.lower() == '0x10000008' or ans4.lower() == '10000008'):
        grade += 1
    else:
        wrong.append('q4')
    # question 5
    ans5 = lookup.get('5')
    if ans5 is not None and (ans5.lower() == 't3' or ans5.lower() == 'x28'):
        grade += 1
    else:
        wrong.append('q5')
    if len(wrong) == 5:
        return (0, utils.failed('all answers are wrong... ¯\\_(⊙︿⊙)_/¯'))
    return (grade, utils.passed() if len(wrong) == 0 else utils.incomplete(','.join(wrong)))


# checks ex2.txt
def check_ex2():
    grade = 0
    lookup = utils.parse_form('./ex1/ex2.txt')
    wrong = []
    # question 1
    ans1 = lookup.get('1')
    if ans1 is not None and (ans1.lower() == 't0' or ans1.lower() == 'x5'):
        grade += 1
    else:
        wrong.append('q1')
    # question 2
    ans2 = lookup.get('2')
    if ans2 is not None:
        ans2 = ans2.split(',')
        ok = False
        expected = [['t1', 't2'], ['x6', 'x7'], ['t1', 'x7'], ['x6', 't2']]
        for e in expected:
            if list(sorted(e)) == list(sorted(ans2)):
                ok = True
                grade += 1
                break
        if not ok:
            wrong.append('q2')
    else:
        wrong.append('q2')
    # question 3
    ans3 = lookup.get('3')
    if ans3 is not None:
        ans3 = ans3.split(',')
        ok = False
        expected = [['34', '42'], ['35', '42']]
        for e in expected:
            if e == ans3:
                ok = True
                grade += 1
                break
        if not ok:
            wrong.append('q3')
    else:
        wrong.append('q3')
    # question 4
    ans4 = lookup.get('4')
    if ans4 is not None and ans4 == '40':
        grade += 1
    else:
        wrong.append('q4')
    # question 5
    ans5 = lookup.get('5')
    if ans4 is not None and ans5 == 'b':
        grade += 1
    else:
        wrong.append('q5')
    if len(wrong) == 5:
        return (0, utils.failed('all answers are wrong... ¯\\_(⊙︿⊙)_/¯'))
    return (grade, utils.passed() if len(wrong) == 0 else utils.incomplete(','.join(wrong)))


# checks factorial.s
def check_ex3():
    try:
        # run tests
        grade = 0
        wrong = []
        # factorial of 3
        test1 = ['java', '-jar', 'V-Sim-2.0.0.jar', './ex3/factorial.s', '-notitle', '<<<', '3']
        task = utils.execute(cmd=test1, timeout=5)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        output = task.stdout.decode().strip()
        expected = 'Enter a number: \nresult = 6\n\nvsim: exit(0)'
        if output == expected:
            grade += 15
        else:
            wrong.append('3')
        # factorial of 7
        test2 = ['java', '-jar', 'V-Sim-2.0.0.jar', './ex3/factorial.s', '-notitle', '<<<', '7']
        task = utils.execute(cmd=test2, timeout=5)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        output = task.stdout.decode().strip()
        expected = 'Enter a number: \nresult = 5040\n\nvsim: exit(0)'
        if output == expected:
            grade += 15
        else:
            wrong.append('7')
        # factorial of 8
        test3 = ['java', '-jar', 'V-Sim-2.0.0.jar', './ex3/factorial.s', '-notitle', '<<<', '8']
        task = utils.execute(cmd=test3, timeout=5)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        output = task.stdout.decode().strip()
        expected = 'Enter a number: \nresult = 40320\n\nvsim: exit(0)'
        if output == expected:
            grade += 15
        else:
            wrong.append('8')
        if wrong == 3:
            return (0, utils.failed('all answers are wrong... ¯\\_(⊙︿⊙)_/¯'), '')
        bad = ','.join(wrong)
        return (grade, utils.passed() if len(wrong) == 0 else utils.incomplete('factorial of: %s failed' % bad), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')


# checks list_map.s
def check_ex4():
    try:
        # run tests
        label = 'ms_ex3_fake_label_%s:' % ('0x%08x' % randint(0, 65535))
        replace = 's/square:/%s/g' % label
        utils.execute(cmd=['sed', '-i', '-e', replace, './ex4/list_map.s'])
        utils.execute(cmd=['printf', "'\nsquare:\naddi a0, a0, 1\njr ra\n'", '>>', './ex4/list_map.s'])
        test = ['java', '-jar', 'V-Sim-2.0.0.jar', './ex4/list_map.s', '-notitle']
        task = utils.execute(cmd=test, timeout=5)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        output = task.stdout.decode().strip()
        expected = '9 8 7 6 5 4 3 2 1 0 \n10 9 8 7 6 5 4 3 2 1 \nvsim: exit(0)'
        if output == expected:
            return (45, utils.passed(), '')
        else:
            return (0, utils.failed(), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')


def lab3_riscv():
    not_found = utils.expected_files([
        './ex1/ex1.txt', './ex2/ex2.txt', './ex3/factorial.s',
        './ex4/list_map.s'
    ])
    if len(not_found) == 0:
        ex1_result = check_ex1()
        ex2_result = check_ex2()
        ex3_result = check_ex3()
        ex4_result = check_ex4()
        table = []
        table.append(('1. Intro V-Sim', *ex1_result[0: 2]))
        table.append(('2. Translating from C to RISC-V', *ex2_result[0: 2]))
        table.append(('3. Factorial', *ex3_result[0: 2]))
        table.append(('4. List Map', *ex4_result[0: 2]))
        errors = ''
        errors += utils.create_error('factorial.s', ex3_result[2])
        errors += utils.create_error('list_map.s', ex4_result[2])
        grade = 0
        grade += ex1_result[0]
        grade += ex2_result[0]
        grade += ex3_result[0]
        grade += ex4_result[0]
        grade = round(grade)
        grade = min(grade, 100)
        report = utils.report(table)
        if errors != '':
            report += '\n\nMore Info:\n\n' + errors
        return utils.write_result(grade, report)
    else:
        utils.write_result(0, 'missing files: %s' % (','.join(not_found)))


if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (BYTES, BYTES))
    lab3_riscv()
    utils.fix_ownership()
