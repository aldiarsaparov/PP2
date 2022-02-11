n = input().split()
if len(n) == 1:
    n = int(n[0])
    x = int(input())
else:
    n, x = int(n[0]), int(n[1])

arr = [int(x + 2*i) for i in range(n)]
k = 0
for elem in arr:
    k ^= elem
print(k)

