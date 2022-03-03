def gen():
    for i in range(int(input())):
        yield i**2
print(*gen())
