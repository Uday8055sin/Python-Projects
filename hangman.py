import random

words = ["python", "computer", "programming", "database", "science"]

word = random.choice(words)

guessed_word = ["_"] * len(word)

guessed_letters = []

wrong_guesses = 0
max_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.")

while wrong_guesses < max_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses:", wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:

        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:

        print("Wrong!")
        wrong_guesses += 1

if "_" not in guessed_word:
    print("\n🎉 YOU WON!")
    print("The word was:", word)

else:
    print("\nGAME OVER!")
    print("The word was:", word)