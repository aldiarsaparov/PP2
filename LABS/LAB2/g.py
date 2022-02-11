n = int(input())
d = {}
demons = []
for _ in range(n):
    name, weak = input().split()
    d[weak] = d.get(weak, 0) + 1

n = int(input())
for _ in range(n):
    name, weak, amount = input().split()
    if weak in d.keys():
        d[weak] -= int(amount)

print(f'Demons left: {sum([i for i in d.values() if i>0])}')