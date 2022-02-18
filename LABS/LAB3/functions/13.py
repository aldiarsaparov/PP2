import random

name = input("Hello! What is your name?\n")

print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

found = False
cnt = 0
guess = random.randint(1, 20)

while not found:
    print("Take a guess.\n")

    num = int(input())
    cnt += 1

    if num > guess:
        print("\nYour guess is too big.")
    elif num < guess:
        print("\nYour guess is too low.")
    else:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        found = True