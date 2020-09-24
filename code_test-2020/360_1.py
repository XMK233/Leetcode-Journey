import sys, re
# s = input()
# ss = [s]
########################
ss = []
for line in sys.stdin:
    ss.append(line)
##########################
# ss = [
# "12_Aaqq12",
# "Password123",
# "PASSWORD_123",
# "PaSS^word",
# "12_Aaqq",
# ]
##################################
res = []

def judge(s):
    if len(s) < 8:
        return "Irregular password"
    upper, lower, digit, charactors = 0, 0, 0, 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c == "_" or re.search("\W", c):#c in "~`!@#$%^&*()_+-={}|[]\\:\";\'<>?,./":
            charactors += 1
    if upper * lower * digit * charactors == 0:
        return "Irregular password"
    return "Ok"
for s in ss:
    res.append(judge(s))
for r in res:
    print(r)