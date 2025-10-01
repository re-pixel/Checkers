# Checkers Game

A classic Checkers (Draughts) game implementation in Python with a graphical user interface and an AI opponent.

## Features

- **Interactive GUI**: Play checkers with an intuitive graphical interface built using Tkinter
- **AI Opponent**: Challenge yourself against an AI opponent that uses the minimax algorithm with alpha-beta pruning
- **Game Rules**: 
  - Standard checkers movement (diagonal forward moves for regular pieces)
  - Multiple jump captures are supported
  - Pieces are promoted to kings when reaching the opposite end
  - Kings can move in all diagonal directions
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

3. Tkinter should be included with your Python installation. If not, install it:
   - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
   - **macOS**: Tkinter is included with Python
   - **Windows**: Tkinter is included with Python

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
   - Pieces reaching the opposite end are promoted to kings (shown with a white dot)
   - Kings can move diagonally in all directions

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
- Searches ahead 6 moves deep by default

## AI Strategy

The AI opponent uses a minimax algorithm with the following evaluation criteria:
- **Piece Values**: Regular pieces (1 point), Kings (3 points)
- **Positional Advantage**: Center squares provide bonus value
- **Promotion Proximity**: Pieces closer to promotion are valued higher
- **Mobility**: Number of available legal moves

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built with Python and Tkinter, implementing classic checkers rules with an AI opponent for single-player gameplay.
