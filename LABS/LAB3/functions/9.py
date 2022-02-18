from math import pi

def Area_of_Sphere(radius):
    volume = (4 / 3) * pi * radius**3
    print("The Volume of a Sphere = ", int(volume))

Area_of_Sphere(int(input()))