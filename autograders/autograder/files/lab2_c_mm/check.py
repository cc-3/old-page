import utils
import resource
import subprocess
from pycparser import c_ast


# 195 MiB of memory
BYTES = 195 * 1024 * 1024


# C loop visitor
class LoopCondVisitor(c_ast.NodeVisitor):

    def __init__(self):
        self.found = False

    def visit_While(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_DoWhile(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_Goto(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_If(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_Switch(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_TernaryOp(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_For(self, node):
        self.found = True
        self.generic_visit(node)

    def reset(self):
        self.found = False


# C free call visitor
class FreeCall(c_ast.NodeVisitor):

    def __init__(self):
        self.count = 0

    def visit_FuncCall(self, node):
        if node.name.name.lower() == 'free':
            self.count += 1
        self.generic_visit(node)

    def reset(self):
        self.count = 0


# checks bit ops
def check_ex1():
    try:
        # compile
        task = utils.make(target='bit_ops')
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        # check loops
        v = LoopCondVisitor()
        # flip_bit
        v.visit(utils.find_func(utils.parse_c('ex1/flip_bit'), 'flip_bit'))
        if v.found:
            return (0, utils.failed('[flip_bit] don\'t use loops/conds please... ¯\\_(⊙︿⊙)_/¯'), '')
        # get_bit
        v.visit(utils.find_func(utils.parse_c('ex1/get_bit'), 'get_bit'))
        if v.found:
            return (0, utils.failed('[get_bit] don\'t use loops/conds please... ¯\\_(⊙︿⊙)_/¯'), '')
        # set_bit
        v.visit(utils.find_func(utils.parse_c('ex1/set_bit'), 'set_bit'))
        if v.found:
            return (0, utils.failed('[set_bit] don\'t use loops/conds please... ¯\\_(⊙︿⊙)_/¯'), '')
        # run tests
        task = utils.execute('./bit_ops', timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        # Output
        output = task.stdout.decode().strip()
        expected = 'OK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\nOK'
        expected = expected.split('\n')
        output = output.split('\n')
        grade = 0
        wrong = 0
        for (exp, out) in zip(expected, output):
            exp = exp.strip()
            out = out.strip()
            if exp == out:
                grade += (100 / 3) / 19
            else:
                wrong += 1
        if wrong == 19:
            return (0, utils.failed('all tests failed...'), '')
        elif wrong != 0:
            return (round(grade), utils.incomplete('some tests failed...'), '')
        else:
            return (100 / 3, utils.passed(), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')


# checks lfsr calculate
def check_ex2():
    try:
        # compile
        task = utils.make(target='lfsr')
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        # check loops
        v = LoopCondVisitor()
        # flip_bit
        v.visit(utils.find_func(utils.parse_c('ex2/lfsr_calculate'), 'lfsr_calculate'))
        if v.found:
            return (0, utils.failed('don\'t use loops/conds please... ¯\\_(⊙︿⊙)_/¯'), '')
        # run tests
        task = utils.execute('./lfsr', timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        # Output
        output = task.stdout.decode().strip()
        f = open('ex2.expected', 'r')
        expected = f.read().strip()
        f.close()
        if output == expected:
            return (100 / 3, utils.passed(), '')
        else:
            return (0, utils.failed('LFSR not working correctly...'), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')


# checks vector
def check_ex3():
    try:
        # compile
        task = utils.make(target='vector')
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        # check for free calls
        v = FreeCall()
        ast = utils.parse_c('ex3/vector')
        # vector_new
        v.reset()
        v.visit(utils.find_func(ast, 'vector_new'))
        if v.count == 0:
            return (0, utils.failed('[vector_new] don\'t forget to call free... ¯\\_(⊙︿⊙)_/¯'), '')
        # vector_delete
        v.reset()
        v.visit(utils.find_func(ast, 'vector_delete'))
        if v.count < 2:
            return (0, utils.failed('[vector_delete] don\'t forget to call free... ¯\\_(⊙︿⊙)_/¯'), '')
        # vector_set
        v.reset()
        v.visit(utils.find_func(ast, 'vector_set'))
        if v.count == 0:
            return (0, utils.failed('[vector_set] don\'t forget to call free... ¯\\_(⊙︿⊙)_/¯'), '')
        # run tests
        task = utils.execute('./vector', timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        # Output
        output = task.stdout.decode().strip().split('\n')
        f = open('ex3.expected', 'r')
        expected = f.read().strip().split('\n')
        f.close()
        grade = 0
        wrong = 0
        for (exp, out) in zip(expected, output):
            exp = exp.strip()
            out = out.strip()
            if exp == out:
                grade += (100 / 3) / 17
            else:
                wrong += 1
        # grade
        if wrong == 17:
            return (0, utils.failed('all tests failed'), '')
        elif wrong != 0:
            return (round(grade), utils.incomplete('some tests failed...'), '')
        else:
            return (100 / 3, utils.passed(), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')


def lab2_c_mm():
    not_found = utils.expected_files([
        './ex1/flip_bit.c', './ex1/flip_bit.c', './ex1/flip_bit.c',
        './ex2/lfsr_calculate.c', './ex3/vector.c'
    ])
    if len(not_found) == 0:
        table = []
        ex1_result = check_ex1()
        table.append(('1. bit ops', *ex1_result[0: 2]))
        ex2_result = check_ex2()
        table.append(('2. LFSR', *ex2_result[0: 2]))
        ex3_result = check_ex3()
        table.append(('3. vector', *ex3_result[0: 2]))
        errors = ''
        errors += utils.create_error('bit_ops', ex1_result[2])
        errors += utils.create_error('LFSR', ex2_result[2])
        errors += utils.create_error('vector', ex3_result[2])
        grade = 0
        grade += ex1_result[0]
        grade += ex2_result[0]
        grade += ex3_result[0]
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
    lab2_c_mm()
    utils.fix_ownership()
