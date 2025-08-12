import random
name = input("Enter your name: ")
print("Hello, " + name + "! Let's play a word guessing game.")

words = ['rainbow', 'unicorn', 'dragon', 'phoenix', 'mermaid']

word = random.choice(words)

print("Guess the characters.")

guesses = ''

turns = 5

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1
    print()

    if failed == 0:
        print("Congratulations! You've guessed the word: " + word)
        break

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess. You have " + str(turns) + " turns left.")

if turns == 0:
    print("Game over! The word was: " + word)