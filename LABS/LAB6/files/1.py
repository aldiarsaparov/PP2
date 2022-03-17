import os

path = input()
os.chdir(path)

dirs = os.listdir(os.getcwd())
for i in dirs:
    if os.path.isdir(i):
        print("directories", i)
    elif os.path.isfile(i):
        print("files", i)
print("all", os.listdir(os.getcwd()))