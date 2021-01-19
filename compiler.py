
import funcs

imps = {}

def get_imps():
    global imps
    out = ""
    for imp in imps:
        out += imps[imp]
    return out

#def get_command(nl):
#    return nl

def insert(s, i, t):
    return s[:i] + t + s[i:]

def compile(code):
    global imps
    compiled = "## compiled by py-pro\n" + code

    #for nl in code.split("\n"):
    #    compiled += "\n" + get_command(nl)
    compiled, imp = funcs.replace(compiled)
    imps.update(imp)
    
    compiled = insert(compiled, compiled.find("\n"), "\n"+get_imps())

    return compiled

def compile_file(filename, outfile):
    with open(filename, "r") as code:
        code = compile(code.read())
    with open(outfile, "w") as out:
        out.write(code)
