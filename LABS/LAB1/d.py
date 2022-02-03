n = int(input())
ch = input()
if ch == "k":
    c = int(input())
    print(round(n / 1024, c))
else:
    print(n * 1024)