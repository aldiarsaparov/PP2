import os 

with open("test.txt", "w") as f:
    x = input().split()
    f.write(str(x))