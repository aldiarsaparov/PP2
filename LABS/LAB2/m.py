str = []
s = []
d = ""

while d != "0":
    s = input().split()
    d = s[0]
    if d == "0":
        break
    else:
        m, y = s[1], s[2]
    str.append((y, m, d))
for y, m, d in sorted(str):
    print(d, m, y)
