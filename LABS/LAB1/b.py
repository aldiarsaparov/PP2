dish = str(input())
k = 0
for x in dish:
    k += ord(x)

if (int(k) > 300):
    print ("It is tasty!")
else:
    print ("Oh, no!")