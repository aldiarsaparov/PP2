from math import tan, pi

sides = int(input())
length = int(input())
area = sides * (length**2) / (4 * tan(pi/sides))
print(f"Input number of sides: {sides}")
print(f"Input the length of a side: {length}")
print(f"The area of the polygon is: {int(area)}")