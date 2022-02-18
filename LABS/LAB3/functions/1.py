def grToou(grams):
    ounces = grams / 28.3495231
    return ounces

n = float(input("The weight in grams: "))
print("The weight in ounces: ", grToou(n))