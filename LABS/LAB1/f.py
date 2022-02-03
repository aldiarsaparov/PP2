for _ in range(int(input())):
    a = int(input())
    if 10 < a <= 25:
        print("You are weak")
    elif 25 < a <= 45:
        print("Okay, fine")
    elif a > 45:
        print("Burn! Burn! Burn Young!")
    elif a <= 10:
        print("Go to work!")
