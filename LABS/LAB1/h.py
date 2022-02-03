s, t = input(), input()
cnt = s.count(t)

if cnt == 1:
    print(s.index(t))
elif cnt >= 2:
    print(s.index(t), s.rindex(t)) 