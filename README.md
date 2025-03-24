# QueensGambit Chess Engine

## Overview
QueensGambit is a Python-based chess engine that utilizes the Minimax algorithm with alpha-beta pruning to evaluate and make optimal moves. It features relative piece values inspired by AlphaZero and includes an entropy-based evaluation for more dynamic gameplay. The engine can play against a human opponent or simulate a match between two AI instances.

<div style="text-align: center;">
  <img src="./chess.png" alt="Preview" style="width: 100%;">
</div>

---

1. **Minimax Algorithm**: Minimax is fundamental for decision-making in game theory and chess AI. It works by recursively evaluating possible moves to determine the optimal move for the current player assuming the opponent plays optimally. This is essential because without such a method, evaluating all possible moves to the end of the game (especially considering the branching factor of chess) would be computationally infeasible.

2. **Depth-Pruning**: Depth-pruning limits the depth to which the minimax algorithm explores possible moves. This is critical in chess because it helps balance between depth of search (finding better moves) and computational feasibility. Without depth-pruning, the search space would grow exponentially, making it impractical to compute.

3. **Alpha-Beta Pruning**: Alpha-beta pruning further enhances efficiency by pruning branches of the search tree that cannot possibly influence the final decision. It reduces the number of nodes evaluated by the minimax algorithm by taking advantage of bounds (alpha and beta values) to discard irrelevant subtrees. This technique significantly speeds up the search process in chess AI.

Given the vast number of possible chess board positions (estimated around **1e43** to **1e50**), these techniques are indispensable. They allow chess engines to make intelligent decisions within a reasonable time frame by narrowing down the search space and focusing on the most promising moves. Without them, achieving competitive playing strength would be nearly impossible due to the sheer computational complexity involved.

## Library Installations
Before using QueensGambit, make sure you have the following libraries installed:
- **python-chess**: Used for chess board representation and move generation. 
  ```bash
  pip install python-chess
  ```

## Features

- **Minimax Algorithm**: Implements the Minimax algorithm with alpha-beta pruning to efficiently evaluate possible moves.
- **AlphaZero Relative Piece Values**: Uses values inspired by AlphaZero for more accurate move evaluations.
- **Entropy-Based Evaluation**: Adds a random factor to the evaluation function for unpredictable gameplay.
- **Opening Catalyst**: Provides a bonus for the number of legal moves in the opening phase.
- **Human vs. AI and AI vs. AI**: Allows for both human vs. AI and AI vs. AI matches.
- **SVG Board State Saving**: Saves the current board state as an SVG file after each move.
- **Difficulty Levels**: Offers four difficulty levels (easy, medium, difficult, auto).
- **Bot Mode**: Option for a more optimized and intelligent gameplay experience.
- **Crazy Mode**: Option for a more random and unpredictable gameplay experience.

## Code Structure
The implementation is structured into several key components:

### `Engine` Class
- **Initialization (`__init__`):**
  - Initializes the chessboard, engine color (maximizing agent), maximum search depth, and other parameters.
  
- **Evaluation Functions:**
  - `checkmate_opportunity()`: Evaluates if the game is in a checkmate position and assigns scores accordingly.
  - `opening_catalyst()`: Provides a bonus for moves made in the opening phase of the game.
  - `evaluation_function()`: Combines the above evaluations to compute a total score for a given board position.
  - `piece_relative_value(position)`: Assigns relative values to each piece type on the board. You can find more information on relative piece value in chess in this paper: [Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess](https://arxiv.org/pdf/2009.04374) by Tomašev et al. (DeepMind, 2020).

- **Minimax Algorithm:**
  - `max_value(depth, alpha, beta)`: Implements the maximizing agent's logic using minimax with alpha-beta pruning.
  - `min_value(depth, alpha, beta)`: Implements the minimizing agent's logic using minimax with alpha-beta pruning.
  - `get_best_move()`: Initiates the search for the best move using the minimax algorithm.

### Game Functions

- `save_board_state()`: Saves the current board state as an SVG file.
- `play_engine_move()`: Executes a move by the AI and saves the board state.
- `play_human_move()`: Prompts the human player to make a move and updates the board state.
- `start_game()`: Alternates moves between the human player and the AI until the game is over.
- `get_user_input()`: Collects user preferences for color, difficulty level, and bot/crazy mode.

### Main Execution
- **Main Function (`main()`):**
  - Entry point of the program, which initializes the game by calling `get_user_input()`.

## Usage

1. **Clone the repository**:

```bash
git clone https://github.com/kanavgoyal898/queensgambit.git
cd queensgambit
```

2. **Run the main script**:

```bash
cd models
python main.py
```

3. **Follow the prompts** to choose your color, difficulty level, and whether you want to play in bot/crazy mode.

## User Interface 
To view SVG files using the Live Server extension in Visual Studio Code, follow these steps:

1. **Install Live Server Extension**:
  - Open Visual Studio Code.
  - Go to the Extensions view by clicking on the square icon on the left sidebar or by pressing `Cmd+Shift+X`.
  - Search for "Live Server" in the Extensions Marketplace.
  - Click "Install" to install the extension.

2. **Open SVG File**:
  - After running the QueensGambit Chess Engine and generating the `chess_board.svg` file in your project directory, locate the file in the Visual Studio Code Explorer.

3. **Activate Live Server**:
  - Right-click on `chess_board.svg` in the Explorer.
  - Select "Open with Live Server" from the context menu.

4. **View SVG in Browser**:
  - Visual Studio Code will automatically open your default web browser and display the SVG file using Live Server.
  - The SVG file will update automatically whenever changes are saved in the editor.

5. **Interact with SVG**:
  - You can interact with the SVG file in the browser as it updates in real-time based on the current state of the chessboard generated by QueensGambit.

6. **Close Live Server**:
  - To stop Live Server, click on the "Close Preview" button in the top-right corner of the browser tab that opened the SVG file.

By following these steps, you can use the Live Server extension in Visual Studio Code to dynamically view and interact with SVG files such as `chess_board.svg` generated by QueensGambit during gameplay.

## Additional Notes

- **Undo Move:** Typing "UNDO" allows the user to undo their last move.
- **End Game:** Typing "END" terminates the game.
- **Outcome:** After the game ends, the result (win/lose/draw) is displayed.`