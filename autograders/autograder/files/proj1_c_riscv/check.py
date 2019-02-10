import os
import utils
import resource
import traceback
import subprocess


# 195 MiB of memory
BYTES = 195 * 1024 * 1024


# reads a file
def read(file):
    f = open(file, 'r')
    text = f.read()
    f.close()
    return text.strip()


# checks part1.c
def check_part1():
    utils.make(target='clean')
    task = utils.make(target='riscv')
    if task.returncode != 0:
        return (0, utils.failed('compilation error'), task.stderr.decode().strip())
    grade = 0
    files = list(map(lambda x: x.split('.')[0].strip(), os.listdir('./riscvcode/code')))
    frac = 50 / len(files)
    errors = []
    for test in files:
        try:
            task = utils.execute(cmd=['./riscv', '-d', 'riscvcode/code/%s.input' % test])
            if task.returncode == 0:
                output = task.stdout.decode().strip()
                expected = read('./riscvcode/ref/%s.solution' % test)
                if output == expected:
                    grade += frac
                else:
                    errors.append('%s not working correctly' % test)
            else:
                errors.append('%s RUNTIME ERROR (%s)' % (test, task.stderr.decode().strip()))
        except subprocess.TimeoutExpired:
            errors.append('%s TIMEOUT' % test)
        except MemoryError:
            errors.append('%s MEMORY EXCEEDED' % test)
        except Exception:
            traceback.print_exc()
            errors.append('%s UNEXPECTED EXCEPTION' % test)
    if len(errors) == len(files):
        return (0, utils.failed('all tests failed'), '\n'.join(errors))
    elif len(errors) != 0:
        return (round(grade), utils.incomplete('some tests failed'), '\n'.join(errors))
    else:
        return (50, utils.passed(), '')


# checks part2.c
def check_part2():
    utils.make(target='clean')
    task = utils.make(target='riscv')
    if task.returncode != 0:
        return (0, utils.failed('compilation error'), task.stderr.decode().strip())
    grade = 0
    files = list(map(lambda x: x.split('.')[0].strip(), os.listdir('./riscvcode/code')))
    frac = 50 / len(files)
    errors = []
    for test in files:
        try:
            task = utils.execute(cmd=['./riscv', '-r', 'riscvcode/code/%s.input' % test])
            if task.returncode == 0:
                output = task.stdout.decode().strip()
                expected = read('./riscvcode/ref/%s.trace' % test)
                if output == expected:
                    grade += frac
                else:
                    errors.append('%s not working correctly' % test)
            else:
                errors.append('%s RUNTIME ERROR (%s)' % (test, task.stderr.decode().strip()))
        except subprocess.TimeoutExpired:
            errors.append('%s TIMEOUT' % test)
        except MemoryError:
            errors.append('%s MEMORY EXCEEDED' % test)
        except Exception:
            traceback.print_exc()
            errors.append('%s UNEXPECTED EXCEPTION' % test)
    if len(errors) == len(files):
        return (0, utils.failed('all tests failed'), '\n'.join(errors))
    elif len(errors) != 0:
        return (round(grade), utils.incomplete('some tests failed'), '\n'.join(errors))
    else:
        return (50, utils.passed(), '')


def proj1_c_riscv():
    not_found = utils.expected_files(['./utils.c', './part1.c', './part2.c'])
    if len(not_found) == 0:
        table = []
        part1_result = check_part1()
        table.append(('1. Disassemble', *part1_result[0: 2]))
        part2_result = check_part2()
        table.append(('2. Execute', *part2_result[0: 2]))
        errors = ''
        errors += utils.create_error('Part 1', part1_result[2])
        errors += '\n' + utils.create_error('Part 2', part2_result[2])
        errors = errors.strip()
        grade = 0
        grade += part1_result[0]
        grade += part2_result[0]
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
    proj1_c_riscv()
    utils.fix_ownership()
