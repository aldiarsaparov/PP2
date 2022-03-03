from math import pi

def conv(degree):
    radian = degree / (180/pi)
    return radian
degree = int(input())
print("radian : ", (conv(degree)))


