a = int(input())
students = {} 

for i in range(a):
    s = (input().split())
    name = str(s[0])
    money = int(s[1])
    if name in students:
        students[name] += money
    else:
        students[name] = money
sortedNames = sorted(students.keys(), key = lambda x : x)
m = max(students.values())

for i in sortedNames:
    if (students[i] == m):
        print(i, "is lucky!")
    else:
        print(i, "has to receive", (m - students[i]), "tenge")