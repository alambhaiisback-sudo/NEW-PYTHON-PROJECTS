import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print("Computer:", computer)

if user == computer:
    print("Draw!")

elif user == "rock" and computer == "scissors":
    print("You Win!")

elif user == "paper" and computer == "rock":
    print("You Win!")

elif user == "scissors" and computer == "paper":
    print("You Win!")

elif user in choices:
    print("Computer Wins!")

else:
    print("Invalid choice!")