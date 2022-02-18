def func(s):
    t = "".join(str(i) for i in s)
    to_remove = "12345689"

    for char in to_remove:
        t = t.replace(char, "")

    if t.find("007") != -1:
        return True
    else:
        return False


print(func([int(i) for i in input().split()]))