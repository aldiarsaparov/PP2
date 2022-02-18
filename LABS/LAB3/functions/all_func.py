def grToou(grams):
    ounces = grams / 28.3495231
    return ounces

def convertFtoC(f):
    c = (5 / 9) * (f - 32)
    return c

def solve(numheads, numlegs):
    chicken = 0
    rabbit = 0

    if numheads >= numlegs:
        print("Error")
    elif numlegs % 2 != 0:
        print("Error")
    else:
        rabbit = (numlegs - 2 * numheads) / 2
        chicken = numheads - rabbit
        return (int(rabbit), int(chicken))