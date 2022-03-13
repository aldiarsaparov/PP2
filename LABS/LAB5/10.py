import re

pattern = "([A-Z][a-z]+)"
pattern1 = r' \1'
print("_".join(re.sub(pattern, pattern1, input()).split()).lower())

# input: PythonisGood