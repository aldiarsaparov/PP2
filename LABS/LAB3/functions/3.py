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
        # print(int(rabbit), int(chicken))
        return (int(rabbit), int(chicken))

numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))