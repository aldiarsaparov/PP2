import os
path = "/home/aldiar/Desktop/2 Semester/PP2/LABS/LAB6"
print("Directories: ")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])

print("Files: ")
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])

print("Files and directories: ")
print([name for name in os.listdit(path)])