import re 

def solution(text):
    pattern = "^[a-z]+_[a-z]+$"
    if re.search(pattern, text):
        return "Found"
    else:
        return "Not found"

print(solution(input()))