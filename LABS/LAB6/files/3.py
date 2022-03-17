import os

path = input()
if os.path.exists(path):
    print("Exists")
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("Does not exist")
