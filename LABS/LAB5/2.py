import re

def solution(text):
    pattern = 'ab{2,3}?'
    if re.search(pattern, text):
        return "Found"
    else:
        return "Not found"

print(solution(input()))