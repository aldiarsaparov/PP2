str = input()
upper = 0
lower = 0
for i in str:
    if (i.islower()):
        lower = lower+1
    elif (i.isupper()):
        upper = upper+1

print("Amount of upper case:", upper)
print("Amount of lower case:", lower)
