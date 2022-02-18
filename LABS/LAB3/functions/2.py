def convertFtoC(f):
    c = (5 / 9) * (f - 32)
    return c

f = float(input("Temperatrue in fahrenheit: "))
print("Temperature in celsius: ", convertFtoC(f))
