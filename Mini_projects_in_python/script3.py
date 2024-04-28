import random

def hangman():
    words = ["hello", "world", "apple","beautiful"]
    word = random.choice(words)
    guessed_letters = set()
    attempts_left = 3

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts_left > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts_left -= 1
            print("Attempts left:", attempts_left)

        print(" ".join(letter if letter in guessed_letters else "_" for letter in word))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            return

    print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()



