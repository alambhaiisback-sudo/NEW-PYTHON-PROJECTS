import random

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)
    print("You got:", dice)

    choice = input("Roll again? (yes/no): ")

    if choice.lower() != "yes":
        print("Game Over!")
        break