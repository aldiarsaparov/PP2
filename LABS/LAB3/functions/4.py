def filter_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(*[num for num in input().split() if filter_prime(int(num))])