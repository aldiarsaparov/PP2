class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
    
    def get_area(self):
        return self.len * self.wid

R1 = Rectangle(int(input()), int(input()))
print(R1.get_area())
