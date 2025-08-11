import random

print("Welcome to the Number Guessing Game!\n You have 7 chances to guess the number. Let's start.")

low = int(input ("Enter the lower bound: "))
high = int(input ("Enter the upper bound: "))

print(f"You have 7 chances to guess a number between {low} and {high}.")

num = random.randint(low, high)
ch = 7      #Total chances
gc = 0      #Guess count

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess:"))

    if guess == num:
        print(f"Congratulations! You've guessed the number {num} correctly.")
        break
    elif guess < num:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

if gc == ch:
    print(f"Sorry, you've used all your chances. The number was {num}.")