def histo(s):
    for i in s:
        print('*' * i)


histo([int(i) for i in input().split()])
