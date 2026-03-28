import random

def get_difficulty():
    print("\n--- Select Difficulty ---")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 200)")
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == '1':
            return 50, "Easy"
        elif choice == '2':
            return 100, "Medium"
        elif choice == '3':
            return 200, "Hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_game(max_num):
    secret = random.randint(1, max_num)
    attempts = 0
    guesses = []

    print(f"\nGuess a number between 1 and {max_num}. Good luck!\n")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > max_num:
            print(f"Out of range! Enter a number between 1 and {max_num}.")
            continue

        attempts += 1
        guesses.append(guess)

        if guess < secret:
            print(f"  Too low!  Try higher. (Attempt #{attempts})")
        elif guess > secret:
            print(f"  Too high! Try lower.  (Attempt #{attempts})")
        else:
            print(f"\n  Correct! The number was {secret}.")
            print(f"  You guessed it in {attempts} attempt{'s' if attempts > 1 else ''}!")
            print(f"  Your guesses: {guesses}")
            return attempts

def main():
    print("=" * 40)
    print("      NUMBER GUESSING GAME")
    print("=" * 40)

    best_score = None
    wins = 0

    while True:
        max_num, level = get_difficulty()
        attempts = play_game(max_num)
        wins += 1

        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"  New best score: {best_score}!")

        print(f"\n  Total wins : {wins}")
        print(f"  Best score : {best_score} attempts")

        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
