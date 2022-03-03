def gen():
    n = int(input())
    for i in range(n, -1, -1):
        yield i

print(*gen())     
