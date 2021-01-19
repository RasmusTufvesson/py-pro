import compiler
import sys

debug = False

on = True
while on:
    com = input(">>> ")
    if com == "exit":
        on = False
    elif com == "help":
        print ("help: helps\nexit: exits the terminal")
    elif com == "debug":
        debug = not debug
    else:
        code = compiler.compile(com)
        if debug:
            print (code)
        try:
            exec(code)
        except BaseException as err:
            print (f"Error:\ncode: {code}\n{str(sys.exc_info())}\n{str(err)}")