import json

exec("func = '"+input("function here(use \\n to separate lines):\n")+"'")
name = input("function name:\n")
rel_name = input("function replace name:\n")

d = json.load(open("functions.json", "r"))

d[name] = [rel_name, "\n"+func]

json.dump(d, open("functions.json", "w"))