import os

with open("test.txt", "r") as f:
    x = f.readlines()
    print(len(x))