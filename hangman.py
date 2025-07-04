import random

# List of 5 predefined words
word_list = ["apple", "grape", "mango", "peach", "melon"]

# Randomly select a word
chosen_word = random.choice(word_list)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Display setup: _ _ _ _
display_word = ["_"] * len(chosen_word)

print("Welcome to Hangman!")
print("Guess the word letter by letter.")
print("You have 6 incorrect guesses.\n")

# Game loop
while wrong_guesses < max_wrong and "_" in display_word:
    print("Word: ", " ".join(display_word))
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Correct!\n")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong!\n")
        wrong_guesses += 1

# Result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Sorry, you lost. The word was:", chosen_word)
print("Game Over!")