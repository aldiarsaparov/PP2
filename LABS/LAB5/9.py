import re

pattern = "[A-Z][a-z]+"
arr = re.findall(pattern, input())

if arr:
    print(*arr, sep=' ')