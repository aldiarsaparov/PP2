n = int(input())
l = []
res = []

for i in range(n):
    inp = input()
    if inp[0] == '1':
        num, name = inp.split(' ')
        l.append(name)
    else:
        res.append(l[0])
        del l[0]
for i in range(len(res)):
    print(res[i], end=' ') 
