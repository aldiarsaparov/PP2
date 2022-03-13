def rev_words(s):
    for i in reversed(s):
        print(*i, sep='', end=' ')


s = input().split()
rev_words(s)
