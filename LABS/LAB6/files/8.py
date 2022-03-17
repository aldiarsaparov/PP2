import os

if os.path.exists(os.getcwd()):
    os.remove(os.path.dirname(__file__)+'/'+'8.txt')
else:
    print('Does not exist')