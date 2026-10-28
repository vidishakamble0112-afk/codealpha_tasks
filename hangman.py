import random

WORDS = ["python", "internship", "program", "keyboard", "developer"]
MAX_WRONG = 6


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        display = " ".join(c if c in guessed else "_" for c in word)
        print("Word:", display)
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print("Guessed letters:", " ".join(sorted(guessed)) or "-")

        if "_" not in display:
            print(f"\nCongratulations! You guessed it: {word}")
            return

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)
        if guess in word:
            print("Good guess!\n")
        else:
            wrong += 1
            print("Wrong guess!\n")

    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()
