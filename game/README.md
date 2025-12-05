# Mini Games Collection

A collection of classic games implemented with Python's Tkinter GUI framework. These games demonstrate GUI development, game logic, and event handling.

## Games Included

### 1. Minesweeper Game

Classic Minesweeper implementation with:

- Configurable grid size and mine count
- Left-click to reveal cells
- Right-click to place/remove flags
- Auto-reveal empty regions
- Win/loss detection

**Files:**

- `main.py` - Main game window and logic
- `cell.py` - Cell class representing each game cell
- `setting.py` - Game configuration and constants
- `utils.py` - Utility functions

### 2. Snake Game

Classic Snake game with:

- Arrow key or WASD controls
- Food collection mechanics
- Body collision detection
- Score tracking
- Increasing difficulty

**Files:**

- `main.py` - Main game loop and rendering
- `cell.py` - Cell/segment representation
- `setting.py` - Game configuration
- `utils.py` - Helper functions

### 3. Tic-Tac-Toe

Two-player Tic-Tac-Toe game featuring:

- 3x3 game board
- Turn-based gameplay
- Win condition detection
- Draw scenario handling
- GUI with buttons for each position

## Features

- ✅ Type hints for better code clarity
- ✅ Comprehensive docstrings
- ✅ Modular architecture
- ✅ Error handling
- ✅ Cross-platform compatibility

## Requirements

- Python 3.12+
- tkinter (usually included with Python)
- PIL/Pillow (for image handling)

## Installation

```bash
pip install pillow
```

## How to Run

**Minesweeper:**

```bash
python minesweeper_game/main.py
```

**Snake:**

```bash
python snake_game/main.py
```

**Tic-Tac-Toe:**

```bash
python tic_tac_toe/main.py
```

## Learning Points

- Object-Oriented Programming (Classes and inheritance)
- GUI Development (Tkinter framework usage)
- Event Handling (Keyboard and mouse input)
- Game Logic (Turn-based and real-time systems)
- State Management (Game state tracking)
- Collision Detection (Geometric calculations)
- Recursion (Used in Minesweeper cell reveal)
- Data Structures (Lists, dictionaries for game state)

---

**Last Updated:** December 2025
