from itertools import permutations

def allPermutations(s):

    for word in permutations(s):
        print(*word, sep ='', end="\n")

allPermutations(input())