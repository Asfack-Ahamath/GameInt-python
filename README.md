# GameInt

Welcome to GameInt, a fun and engaging color guessing game built in Python. This game challenges players to guess a randomly generated color code within a limited number of attempts. Each guess provides feedback to help you get closer to the correct answer. Dive in and test your deduction skills!

## Features

- **Colorful Interface:** Utilizes the `colorama` library to make the CLI colorful and engaging.
- **Intuitive Gameplay:** Simple yet challenging gameplay that's easy to understand but hard to master.
- **Feedback Mechanism:** Each guess provides clear feedback to guide your next attempt, with points awarded for accuracy.

## How to Play

1. **Start the Game:** Run the script and choose to start the game.
2. **Enter Your Name:** Customize your experience by entering your name.
3. **Guess the Color Code:** Use the hints provided after each guess to deduce the correct color code.
4. **Winning:** Correctly guess the color code within 8 attempts to win.
5. **Exiting the Game:** Enter `0000` at any prompt to exit the game early.

## Rules

- The game will generate a 4-digit color code, where each digit represents a unique color.
- Colors are mapped from 1 to 6 [White, Blue, Red, Yellow, Green, Purple].
- Each guess should be a sequence of 4 digits (e.g., 1234).
- You have 8 attempts to guess the correct code.
- Points are awarded based on the accuracy of each guess:
  - Correct color and position: 15 points.
  - Correct color but wrong position: 5 points.
- The game ends either when the correct code is guessed or attempts are exhausted.
