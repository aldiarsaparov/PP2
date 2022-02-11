size = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
    
print(arr[-1]*arr[-2])