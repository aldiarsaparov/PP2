n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0:
            print(j, end=' ')
        elif j == 0:
            print(i, end=' ')
        elif i == j:
            print(j * j, end=' ')
        else:
            print(0, end=' ')
    print('')