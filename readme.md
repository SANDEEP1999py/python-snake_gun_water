# 🐍 Snake, Water, Gun – AI Powered Game

This is a simple yet smart implementation of the **Snake, Water, Gun** game built in Python. The computer's move is generated using the **Linear Congruential Generator (LCG)** algorithm, while the game logic is handled using a **matrix-based resolution method**.

---

## 🎮 Game Overview

- **User vs Computer** gameplay.
- Computer's move is pseudo-random, generated via the **LCG** algorithm.
- Winner is determined using a **3x3 decision matrix**.
- Clean CLI-based interface for a smooth playing experience.

---

## 🧠 Core Concepts Used

### 🔢 Linear Congruential Generator (LCG)

Used to generate the computer’s move with controlled randomness.

Formula:
Xₙ₊₁ = (a * Xₙ + c) % m


### 🧮 Matrix-Based Winner Resolution

A matrix determines the outcome of all move combinations:
the win and lose for the User.

|              | Snake(1) | Water(2) | Gun(3)   |
|--------------|----------|--------|------------|
| **Gun(1)**   | Lose     | Win    | Draw       |
| **Water(2)** | Win      | Draw   | Lose       |
| **Snake(3)** | Draw     | Lose   | Win        |

---

## 🚀 How to Run

1. Clone this repository:
```bash

2. Run the game.
python main_.py
