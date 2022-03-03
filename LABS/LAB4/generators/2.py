def gen():
    for i in range(int(input())):
        if i % 2 == 0:
            yield i
print(*gen(), sep =',')