#print(*[i for i in input().split() if len(i) >= 3])

lst = input().split()

for i in range(len(lst)):
    if len(lst[i]) >= 3:
        print(lst[i], end = ' ')