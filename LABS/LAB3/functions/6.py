def rev_words(s):
    for i in reversed(s):
        print(*i, sep='', end=' ')


s = input().split()
rev_words(s)

# In our program, we have used reversed() to get the iterator that
#  accesses the given sequence in the reverse order. And to add the words in the new string,
# we have used join() which will join all the words with a space in the new string.
