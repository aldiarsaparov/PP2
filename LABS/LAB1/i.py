check = "@gmail.com"
for i in range(int(input())):
    s = input()
    if s.endswith(check): #	Returns true if the string ends with the specified value
        print(s.replace(check, ""))