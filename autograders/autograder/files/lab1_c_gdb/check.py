import utils
import resource
import subprocess


# 195 MiB of memory
BYTES = 195 * 1024 * 1024


def check_eccentric():
    try:
        task = utils.make(target='test_eccentric')
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        task = utils.execute('./test_eccentric', timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        # Output
        output = task.stdout.decode().strip()
        expected = 'V0 OK\nV1 OK\nV2 OK\nV3 OK'
        expected = expected.split('\n')
        output = output.split('\n')
        grade = 0
        wrong = 0
        for (exp, out) in zip(expected, output):
            exp = exp.strip()
            out = out.strip()
            if exp == out:
                grade += 25/4
            else:
                wrong += 1
        return (round(grade), utils.passed() if wrong == 0 else utils.incomplete('some answers are wrong...'), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')


def check_cgdb():
    output = utils.parse_form('ex2.txt')
    expected = {'1': 'b', '2': 'c', '3': 'd', '4': 'b', '5': 'c', '6': 'c', '7': 'a', '8': 'a', '9': 'b'}
    grade = 0
    wrong = []
    for key in expected.keys():
        out = output.get(key)
        exp = expected.get(key)
        if exp == out:
            grade += 25/9
        else:
            wrong.append('q'+key)
    return (round(grade), utils.passed() if len(wrong) == 0 else utils.incomplete(','.join(wrong)))


def check_equal():
    try:
        task = utils.make(target='test_ll_equal')
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        task = utils.execute('./test_ll_equal', timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('cuntime error'), task.stderr.decode().strip())
        output = task.stdout.decode().strip()
        expected = 'OK\nOK\n'
        expected = expected.strip()
        grade = 0
        if expected == output:
            grade += 25
        return (grade, utils.passed() if grade == 25 else utils.failed('failed some tests...'), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception:
        return (0, utils.failed('memory limit exceeded'), '')


def check_ll_cycle():
    try:
        task = utils.make(target='test_ll_cycle')
        if task.returncode != 0:
            return (0, utils.failed('Compilation error'), task.stderr.decode().strip())
        task = utils.execute('./test_ll_cycle', timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('Runtime error'), task.stderr.decode().strip())
        output = task.stdout.decode().strip()
        expected = 'OK\nOK\nOK\nOK\nOK\nOK\n'
        expected = expected.strip()
        grade = 0
        if expected == output:
            grade += 25
        return (grade, utils.passed() if grade == 25 else utils.failed('Failed some tests...'), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception:
        return (0, utils.failed('memory limit exceeded'), '')


def lab1_c_gdb():
    not_found = utils.expected_files(['./eccentric.c', './ex2.txt', './ll_equal.c', './ll_cycle.c'])
    if len(not_found) == 0:
        table = []
        eccentric = check_eccentric()
        table.append(['1. eccentric', eccentric[0], eccentric[1]])
        cgdb = check_cgdb()
        table.append(['2. CGDB', cgdb[0], cgdb[1]])
        ll_equal = check_equal()
        table.append(['3. ll_equal', ll_equal[0], ll_equal[1]])
        ll_cycle = check_ll_cycle()
        table.append(['5. ll_cycle', ll_cycle[0], ll_cycle[1]])
        grade = 0
        grade += eccentric[0]
        grade += cgdb[0]
        grade += ll_equal[0]
        grade += ll_cycle[0]
        errors = ''
        errors += utils.create_error('eccentric.c', eccentric[2])
        errors += utils.create_error('ll_equal.c', ll_equal[2])
        errors += utils.create_error('ll_cycle.c', ll_cycle[2])
        grade = min(grade, 100)
        report = utils.report(table)
        if errors != '':
            report += '\n\nMore Info:\n\n' + errors
        return utils.write_result(grade, report)
    else:
        utils.write_result(0, 'missing files: %s' % (','.join(not_found)))


if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (BYTES, BYTES))
    lab1_c_gdb()
