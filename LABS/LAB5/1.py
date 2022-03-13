import re

def solution(text):
        pattern = 'ab*?'
        if re.search(pattern,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(solution(input()))