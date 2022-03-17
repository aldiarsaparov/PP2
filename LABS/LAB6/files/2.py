import os
k = input()
print('Exist:', os.access(k, os.F_OK))
print('Readable:', os.access(k, os.R_OK))
print('Writable:', os.access(k, os.W_OK))
print('Executable:', os.access(k, os.X_OK))
