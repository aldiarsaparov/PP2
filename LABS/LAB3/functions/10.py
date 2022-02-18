def toSet(first):
    second = []

    for num in first:
        if num not in second:
            second.append(num)

    return second

first = [int(i) for i in input().split()]
print(*toSet(first))