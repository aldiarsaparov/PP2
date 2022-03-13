import re

def sol(s):
    st = ""
    for i in range(len(s)):
        if s[i - 1] == "_":
            st += s[i].upper()
        else:
            st += s[i]
    return st

print(re.sub("_", "", sol(input())))
