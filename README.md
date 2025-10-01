# Checkers Game

A classic Checkers (Draughts) game implementation in Python with a graphical user interface and an AI opponent.

## Features

- **Interactive GUI**: Play checkers with an intuitive graphical interface built using Tkinter
- **AI Opponent**: Challenge yourself against an AI opponent that uses the minimax algorithm with alpha-beta pruning
- **Game Rules**: 
  - Standard checkers movement (diagonal forward moves for regular pieces)
  - Multiple jump captures are supported
  - Pieces are promoted to queens when reaching the opposite end
  - Queens can move in all diagonal directions
- **Visual Feedback**: See possible moves highlighted when selecting a piece

## Requirements

- Python 3.x
- tkinter (usually included with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/re-pixel/Checkers.git
cd Checkers
```

2. Ensure you have Python 3 installed:
```bash
python --version
```

## Usage

Run the game by executing:
```bash
python main.py
```

## How to Play

1. **Start the Game**: When you launch the game, the board is displayed with red pieces (yours) at the bottom and black pieces (AI) at the top.

2. **Making Moves**:
   - Click on one of your red pieces to select it
   - Valid moves will be highlighted with gray circles
   - Click on a highlighted position to move your piece
   - The AI will automatically make its move after yours

3. **Game Rules**:
   - Regular pieces move diagonally forward one square
   - Capture opponent pieces by jumping over them
   - Multiple captures must be made if available
   - Pieces reaching the opposite end are promoted to queens (shown with a white dot)
   - Queens can move diagonally in all directions

4. **Winning**: The game ends when one player has no legal moves left or no pieces remaining.

## Project Structure

```
Checkers/
├── main.py         # Entry point for the application
├── gui.py          # GUI implementation using Tkinter
├── board.py        # Board logic and game rules
├── computer.py     # AI opponent using minimax algorithm
└── README.md       # This file
```

## Game Components

### Board (`board.py`)
- Manages the game board state (8x8 grid)
- Handles piece movement and capture logic
- Validates legal moves for each piece
- Supports move undo for AI simulation

### GUI (`gui.py`)
- Renders the checkerboard and pieces
- Handles user input (mouse clicks)
- Displays possible moves
- Manages game flow between player and AI

### Computer (`computer.py`)
- Implements minimax algorithm with alpha-beta pruning
- Evaluates board positions based on:
  - Piece count and type (regular pieces vs. kings)
  - Board position (center control)
  - Promotion potential
  - Available moves
- Configurable search depth

## AI Strategy

The AI opponent uses a minimax algorithm with the following evaluation criteria:
- **Piece Values**: Regular pieces (1 point), Kings (3 points)
- **Positional Advantage**: Center squares provide bonus value (+0.5 points)
- **Promotion Proximity**: Pieces closer to promotion are valued higher (+0.75 points)
- **Mobility**: Number of available legal moves - the position evaluation takes into account the difference in the number of legal moves (weighted by the factor of 0.1)
