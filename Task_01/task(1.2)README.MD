# 🎯 Task 01 (1.2) – Number Guessing Game (Python)

## 📌 Description

This Python program is a **number guessing game** where the computer randomly selects a number between 1 and 100, and the player must guess it. The program provides hints to the user whether the guess is too low or too high until the correct number is guessed.

---

## 🧠 How It Works

- The program uses the `random` module to generate a random number between 1 and 100.
- A `while` loop continues until the user guesses the correct number.
- After each guess:
  - If the guess is **lower** than the number, it prompts: `"Guess higher!"`
  - If the guess is **higher** than the number, it prompts: `"Guess lower!"`
  - When the guess is correct, it prints: `"You won!"`

---

## 🛠️ Technologies Used

- Python
- Built-in `random` module

---

## 📄 Sample Output

```bash
Enter Guess: 40
Guess higher!
Enter Guess: 70
Guess lower!
Enter Guess: 65
Guess lower!
Enter Guess: 60
You won!
```
