# 🐍 Task 04 – Snake Game using Tkinter

## 📌 Description

This project is a **classic Snake Game** built using Python’s `tkinter` module. It features a moving snake that grows when it eats food, tracks the player's score, and ends the game on collisions. The game runs in a GUI window and supports real-time keyboard input for controlling the snake.

---

## 🎮 Game Features

- Snake movement controlled via **arrow keys**.
- Real-time gameplay with **10 frames per second** update loop.
- Score tracking and game over screen.
- Snake grows with each food item eaten.
- Collision detection with self and walls.
- Game window is **centered** on the screen.

---

## 🧠 Game Mechanics

- The snake and food are drawn on a 25x25 tile grid.
- Movement is grid-based, and the snake can move in four directions.
- When the snake eats food:
  - Its body grows by one tile.
  - The score increases.
  - A new food piece is placed randomly on the grid.
- The game ends if the snake:
  - Collides with the screen boundaries.
  - Collides with itself.

---

## 🛠️ Technologies Used

- Python 3.x
- `tkinter` for GUI
- `random` for food placement

---

## 📄 Sample Gameplay Screenshot

*(Optional – You can add a screenshot of the game window here)*

---

## 🚀 How to Run the Game

```bash
# Step 1: Navigate to the game folder
cd Internship_Tasks/Task_04

# Step 2: Run the game
python3 snake_game.py
```
