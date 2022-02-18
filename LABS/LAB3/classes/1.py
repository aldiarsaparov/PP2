class Task1:
    def __init__(self):
        self.get_string = input()
    
    def upperCase(self):
        return self.get_string.upper()
    
res = Task1()
print(res.upperCase())