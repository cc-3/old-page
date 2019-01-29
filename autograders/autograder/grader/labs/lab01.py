from .. import utils


__ALL__ = ['lab1_c_gdb_expected', 'lab1_c_gdb']


lab1_c_gdb_expected = ['eccentric.c', 'ex2.txt', 'll_equal.c', 'll_cycle.c']


def check_eccentric(tmp):
    try:
        task = utils.make(target='test_eccentric', dir=tmp)
        if task.returncode != 0:
            return (0, utils.failed('Compilation error'), task.stderr.decode().strip())
        task = utils.execute('./test_eccentric', dir=tmp, timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('Runtime error'), task.stderr.decode().strip())
        # Output
        output = task.stdout.decode().strip()
        expected = 'V0 OK\nV1 OK\nV2 OK\nV3 OK'
        expected = expected.split('\n')
        output = output.split('\n')
        grade = 0
        for (exp, out) in zip(expected, output):
            exp = exp.strip()
            out = out.strip()
            if exp == out:
                grade += 25/4
        return (grade, utils.passed() if grade == 25 else utils.incomplete('Some answers are wrong...'), '')
    except Exception:
        return (0, utils.failed('TIMEOUT.'), '')


def check_cgdb(tmp):
    output = utils.parse_form(utils.join(tmp, 'ex2.txt'))
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
    return (grade, utils.passed() if len(wrong) == 0 else utils.incomplete(','.join(wrong)))


def check_equal(tmp):
    try:
        task = utils.make(target='test_ll_equal', dir=tmp)
        if task.returncode != 0:
            return (0, utils.failed('Compilation error'), task.stderr.decode().strip())
        task = utils.execute('./test_ll_equal', dir=tmp, timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('Runtime error'), task.stderr.decode().strip())
        output = task.stdout.decode().strip()
        expected = 'OK\nOK\n'
        expected = expected.strip()
        grade = 0
        if expected == output:
            grade += 25
        return (grade, utils.passed() if grade == 25 else utils.failed('Failed some tests...'), '')
    except Exception:
        return (0, utils.failed('TIMEOUT'), '')


def check_ll_cycle(tmp):
    try:
        task = utils.make(target='test_ll_cycle', dir=tmp)
        if task.returncode != 0:
            return (0, utils.failed('Compilation error'), task.stderr.decode().strip())
        task = utils.execute('./test_ll_cycle', dir=tmp, timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('Runtime error'), task.stderr.decode().strip())
        output = task.stdout.decode().strip()
        expected = 'OK\nOK\nOK\nOK\nOK\nOK\n'
        expected = expected.strip()
        grade = 0
        if expected == output:
            grade += 25
        return (grade, utils.passed() if grade == 25 else utils.failed('Failed some tests...'), '')
    except Exception:
        return (0, utils.failed('TIMEOUT'), '')


def lab1_c_gdb(tmp, token):
    table = []
    eccentric = check_eccentric(tmp)
    table.append(['EX1: eccentric', eccentric[0], eccentric[1]])
    cgdb = check_cgdb(tmp)
    table.append(['EX2: CGDB', cgdb[0], cgdb[1]])
    ll_equal = check_equal(tmp)
    table.append(['Ex3: ll_equal', ll_equal[0], ll_equal[1]])
    ll_cycle = check_ll_cycle(tmp)
    table.append(['Ex5: ll_cycle', ll_cycle[0], ll_cycle[1]])
    grade = 0
    grade += eccentric[0]
    grade += cgdb[0]
    grade += ll_equal[0]
    grade += ll_cycle[0]
    errors = ''
    errors += utils.create_error('eccentric.c', eccentric[2])
    errors += utils.create_error('ll_equal.c', ll_equal[2])
    errors += utils.create_error('ll_cycle.c', ll_cycle[2])
    return (grade, table, errors)
