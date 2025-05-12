# ✊🖐✌️ Task 02 – Rock, Paper, Scissors Game

## 📌 Description

This Python program is a terminal-based implementation of the classic **Rock, Paper, Scissors** game, where the user plays against the computer. The game continues in a loop and keeps track of scores until the user chooses to quit.

---

## 🎮 Features

- User inputs:
  - `1` for Rock
  - `2` for Paper
  - `3` for Scissors
  - `x` to quit the game
- Computer makes a random selection each round
- Displays round results and updates scores
- Gracefully exits and displays final scores when quitting

---

## 🧠 Game Logic

- Rock beats Scissors  
- Scissors beats Paper  
- Paper beats Rock  
- Same choice = Tie

---

## 📄 Sample Output

```bash
Enter 1 for Rock, 2 for Paper, or 3 for Scissor. Enter x to quit: 1
Machine selects 'scissors', user selects 'rock'
You win!!!
Current Score: 	Machine = 0, User = 1

Enter 1 for Rock, 2 for Paper, or 3 for Scissor. Enter x to quit: 2
Machine selects 'scissors', user selects 'paper'
Machine wins!!!
Current Score: 	Machine = 1, User = 1

Enter 1 for Rock, 2 for Paper, or 3 for Scissor. Enter x to quit: x
Thanks for playing
Final Score: Machine = 1, User = 1
```
