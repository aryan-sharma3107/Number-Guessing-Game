# Number-Guessing-Game
# 🎯 Number Guessing Game

A fun, interactive command-line game built with Python where you try to guess a randomly generated number. Choose your difficulty, track your best score, and see how few attempts it takes!


## 📸 Demo

========================================
      NUMBER GUESSING GAME
========================================

--- Select Difficulty ---
1. Easy   (1 - 50)
2. Medium (1 - 100)
3. Hard   (1 - 200)
Enter choice (1/2/3): 2

Guess a number between 1 and 100. Good luck!

Your guess: 50
  Too high! Try lower.  (Attempt #1)
Your guess: 25
  Too low!  Try higher. (Attempt #2)
Your guess: 37
  Correct! The number was 37.
  You guessed it in 3 attempts!
  Your guesses: [50, 25, 37]
```

## ✨ Features

- 🟢 **3 Difficulty Levels** — Easy (1–50), Medium (1–100), Hard (1–200)
- 🔁 **Play Again** — Keep playing without restarting the program
- 🏆 **Best Score Tracking** — Tracks your lowest attempt count across rounds
- 📊 **Guess History** — Displays all your guesses at the end of each round
- ✅ **Input Validation** — Handles invalid input gracefully (letters, out-of-range numbers)


## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- No external libraries required — uses only the built-in `random` module

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   ```

2. Navigate into the project folder:
   ```bash
   cd number-guessing-game
   ```

3. Run the game:
   ```bash
   python number_guessing_game.py
   ```


## 🗂️ Project Structure

```
number-guessing-game/
│
├── number_guessing_game.py   # Main game file
└── README.md                 # Project documentation
```


## 🧠 Concepts Used

| Concept | Usage |
|---|---|
| `random.randint()` | Generate a secret random number |
| `while` loops | Keep the game running until correct guess |
| `try / except` | Handle invalid user input |
| Functions | Organize code into `get_difficulty()`, `play_game()`, `main()` |
| f-strings | Format output messages dynamically |
| Lists | Store and display guess history |


## 🎮 How to Play

1. Run the script in your terminal
2. Choose a difficulty level (Easy / Medium / Hard)
3. Enter your guess when prompted
4. The game tells you if your guess is **too high** or **too low**
5. Keep guessing until you find the correct number
6. Try to beat your best score!


## 🛠️ Future Improvements

- [ ] Add a GUI version using Tkinter
- [ ] Add a timer to track how fast you guess
- [ ] Save high scores to a file
- [ ] Add a hint system (e.g., "You're very close!")
- [ ] Multiplayer mode — two players take turns


## 📄 License

This project is open source and available under the [MIT License](LICENSE).


## 🙋‍♂️ Author

Made with ❤️ as a beginner Python project.  
Feel free to fork, improve, and share!
