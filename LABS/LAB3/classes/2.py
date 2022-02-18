class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, len):
        self.length = len

    def get_area(self):
        return self.length**2

S1=Square(int(input()))
print(S1.get_area())