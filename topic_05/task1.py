import random

rules = [
    ("stone", "scissors"),
    ("scissors", "paper"),
    ("paper", "stone")
]

user = input("Enter 'stone', 'scissors', 'paper': ").lower()
computer = random.choice(["stone", "scissors", "paper"])

print("Computer chose: {computer}")

if user == computer:
    print("Draw")
else:
    user_wins = False
    for win, lose in rules:
        if user == win and computer == lose:
            user_wins = True
            break

    if user_wins:
        print("You win")
    else:
        print("Computer wins")