def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

a, b = map(int, input().split())

if a <= 500 and isPrime(a) and b%2==0:
    print("Good job!")
else:
    print("Try next time!")