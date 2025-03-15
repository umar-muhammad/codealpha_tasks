import random

# List of words
word_list = ["python", "computer", "programming", "developer", "hangman"]

# Hangman ASCII stages
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Function to get difficulty level
def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy (8 attempts)")
    print("2. Medium (6 attempts)")
    print("3. Hard (4 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return 8
        elif choice == "2":
            return 6
        elif choice == "3":
            return 4
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

# Function to play Hangman
def play_hangman():
    word = random.choice(word_list)  # Select a random word
    word_display = ["_"] * len(word)  # Hidden word as underscores
    guessed_letters = []
    attempts = choose_difficulty()  # Get difficulty level

    print("\n🎉 Welcome to Hangman!")
    print(" ".join(word_display))  # Show hidden word

    while attempts > 0 and "_" in word_display:
        print("\n" + hangman_stages[min(6, 6 - attempts)])  # Show hangman drawing
        guess = input("Guess a letter: ").lower()

        # Check if the letter is already guessed
        if guess in guessed_letters:
            print("❗ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print("✅ Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            print("❌ Wrong guess! You lose an attempt.")
            attempts -= 1

        print(" ".join(word_display))
        print(f"Attempts left: {attempts}")

    # Final result
    if "_" not in word_display:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print(hangman_stages[-1])  # Show final hangman stage
        print("\n💀 Game Over! The word was:", word)

    # Keep window open until user decides to exit
    input("\nPress 0 and Enter to exit...")

# Run the game
if __name__ == "__main__":
    play_hangman()
