def func(l):
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == 3 and l[j] == 3:
                return True
            else:
                break
    return False

l = [int(i) for i in input().split()]

print(func(l))