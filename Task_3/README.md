# 🎮 Task 03 – Tic Tac Toe (Player vs CPU)

## 📌 Description

This project is a **command-line Tic Tac Toe** game implemented in Python, where the user plays against the computer. The game board is displayed after every move, and the first to align three of their symbols (X for Player, O for CPU) in a row, column, or diagonal wins. If all spots are taken without a winner, the game ends in a draw.

---

## 🧠 Game Mechanics

- **Board**: 3x3 grid represented using a 2D list.
- **Turns**: Alternates between the Player (`X`) and the CPU (`O`).
- **Winning Conditions**:
  - Three of the same symbol in a row, column, or diagonal.
- **Draw Condition**: All 9 positions filled without a winner.

---

## 🛠️ Technologies Used

- Python 3.x
- `random` module for CPU moves

---

## 🕹️ Controls

- Player enters a number from **1 to 9** to place `X` on the board.
- The CPU automatically selects a random unoccupied spot for `O`.

---

## 📄 Sample Gameplay

```bash
Welcome to Tic Tac Toe
----------------------

+---+---+---+
|  1 | 2 | 3 |
+---+---+---+
|  4 | 5 | 6 |
+---+---+---+
|  7 | 8 | 9 |

Choose a number [1-9]: 1

CPU chooses: 5

+---+---+---+
|  X | 2 | 3 |
+---+---+---+
|  4 | O | 6 |
+---+---+---+
|  7 | 8 | 9 |

Choose a number [1-9]: 3

CPU chooses: 9

+---+---+---+
|  X | 2 | X |
+---+---+---+
|  4 | O | 6 |
+---+---+---+
|  7 | 8 | O |

Choose a number [1-9]: 2

CPU chooses: 6

+---+---+---+
|  X | X | X |
+---+---+---+
|  4 | O | O |
+---+---+---+
|  7 | 8 | O |
X has won!

+---+---+---+
|  X | X | X |
+---+---+---+
|  4 | O | O |
+---+---+---+
|  7 | 8 | O |

Game over! Thank you for playing :)
