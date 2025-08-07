import random

while True:
    choice = input("Do you want to roll the dice? (yes/no): ").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1.6)
        print(f"You rolled a {roll}.")
    elif choice == "n":
        print("Okay, maybe next time!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")