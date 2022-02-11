a = input()
s = list(set(a.split()))
s.sort()
print(len(s))

for a in s:
    if a.isalpha():
        print(a)
    else:
        print(a[:-1])
