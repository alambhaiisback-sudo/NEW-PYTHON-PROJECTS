import random

lucky_number = random.randint(1, 10)

print("🎯 Welcome to Lucky Number Game!")

guess = int(input("Guess a number between 1 and 10: "))

if guess == lucky_number:
    print("🎉 Congratulations! You got the Lucky Number!")
else:
    print("❌ Wrong guess!")
    print("Lucky Number was:", lucky_number)