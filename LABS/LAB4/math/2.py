def Area(b1, b2, h):
    return ((b1 + b2) / 2) * h


height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))

print("Area is:", Area(base1, base2, height))
