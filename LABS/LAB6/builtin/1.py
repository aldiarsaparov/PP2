import math
def sol(list):
     return math.prod(list)

list1 = list(map(int, input().strip().split()))
print(sol(list1))