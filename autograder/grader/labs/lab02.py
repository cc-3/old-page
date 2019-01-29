from .. import utils

#Aquí no sé qué va... #:( 
__ALL__ = []

lab2_expected = ['bit_ops.c', 'lfsr.c', 'vector.c']

def check_bit_ops(dir):

    file = open("bit_ops.c", "r")
    file = file.read()
    file = file.split("#ifndef TEST")
    code = file[0]

    check = re.search("\sif |\sif(", code)
    if check == None:
        check = re.search("?", code)
        if check == None:
            check = re.search("\sfor |\sfor(", code)
            if check == None:
                check = re.search("while", code)
                if check == None:
                    check = re.search("switch", code)
                    if check != None:
                        return (0, utils.failed('Using switch structure'), "")
                else:
                    return (0, utils.failed('Using while loop'), "")
            else:
                return (0, utils.failed('Using for loop'), "")
        else:
            return (0, utils.failed('Using ternary operator'), "")
    else:
        return (0, utils.failed('Using if command'), "") 

    try: 
        grade = 0
        task = utils.make(target='test_bits_ops', dir=dir)
        if task.returncode != 0:
            return (0, utils.failed('Compilation error'), task.stderr.decode().strip())
        task = utils.execute('./test_bits_ops', dir=dir, timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('Runtime error'), task.stderr.decode().strip())

        out = task.stdout.decode().strip()
        outQ11 = out[:18]
        outQ12 = out[18:42]
        outQ13 = out[42:]

        expQ11 = "OK\nOK\nOK\nOK\nOK\nOK\n"             #6
        expQ12 = "OK\nOK\nOK\nOK\nOK\nOK\nOK\nOK\n"     #8
        expQ13 = "OK\nOK\nOK\nOK\nOK\n"                 #5

        msg = ""

        if outQ11 == expQ11:
            grade += 10
            msg.append("get_bit, ")
        if outQ12 == expQ12:
            grade += 10
            msg.append("set_bit, ")
        if outQ13 == expQ13:
            grade += 10
            msg.append("flip_bit")
        if(msg == ""):
            return(grade, utils.passed(), "")
        elif(msg == "get_bit, set_bit, flip_bit"):
            return(grade, utils.failed("Verify all functions"), "")
        else:
            return(grade, utils.incomplete("Check the following functions: " + msg))
    except Exception:
        return(0, utils.failed("Exception Error"), "")

def check_lfsr(dir):
    try:
        grade = 0
        task = utils.make(target='test_lfsr', dir=dir)
        if task.returncode != 0:
            return (0, utils.failed('Compilation error'), task.stderr.decode().strip())
        task = utils.execute('./test_lfsr', dir=dir, timeout=1)
        if task.returncode != 0:
            return (0, utils.failed('Runtime error'), task.stderr.decode().strip())

        out = task.stdout.decode().strip()
        expected = "Congratulations! It works!\n"

        if(out == expected):
            grade += 30
            return(grade, utils.passed(), "")
        else:
            return(0, utils.failed("It is not working properly"), "")
    except Exception:
        return(0, utils.failed("Exception error"), "")

def check_vector(dir):
    #Falta verificar que el heap esté vacío al final -> 10
    try:
        grade = 0
        task = utils.make(target='test_vector', dir=dir)
        if task.returncode != 0:
            return (0, utils.failed('Compilation error'), task.stderr.decode().strip())
        task = utils.execute('./test_vector', dir=dir, timeout = 1)
        if task.returncode != 0:
            return (0, utils.failed('Runtime error'), task.stderr.decode().strip())
        
        out = task.stdout.decode().strip()
        out31 = out[:1]
        out32 = out[1:]

        expected = "OK\n"
        msg = ""

        if out31 == expected:
            grade += 15
        else:
            msg.append("vector_new, vector_delete and ")
        
        if out32 == expected:
            grade +=15
        else:
            msg.append("vector set")

        if grade == 40:
            return(grade, utils.passed(), "")
        elif grade == 0:
            return(grade, utils.failed("Not working at all"), "")
        else:
            return(grade, utils.incomplete(msg + "not working"), "")
    except Exception:
        return(0, utils.failed("Exception error"), "")
