
def replace(s):
    global funcs
    line = s
    imports = {}
    for func in funcs:
        #print (line)
        line = line.replace(func, funcs[func][0])
        #print (line)
        if funcs[func][0] in line:
            imports[funcs[func][0]] = funcs[func][1]
    return line, imports



upper = """
def upper(s):
    return str(s).upper()
"""

isupper = """
def isupper(s):
    return str(s).isupper()
"""

lower = """
def lower(s):
    return str(s).lower()
"""

islower = """
def islower(s):
    return str(s).islower()
"""

funcs = {
    "big": ["upper", upper],#[upper, str],
    "isbig": ["isupper", isupper],#[isupper, bool],
    "small": ["lower", lower],#[lower, str],
    "issmall": ["islower", islower]#[islower, bool]
}