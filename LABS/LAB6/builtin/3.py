def sol(s):
    rev = ''.join(reversed(s))

    if (s == rev):
        return True
    return False

s = input()
res = sol(s)

if res:
    print("Yes")
else:
    print("No")