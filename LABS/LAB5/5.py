import re

def solution(text):
    pattern = "a.*?b$"
    if re.search(pattern, text):
        return "Found"
    else:
        return "Not found"

print(solution(input()))