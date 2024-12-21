# Advanced Tic Tac Toe

This is an enhanced version of the classic Tic Tac Toe game, implemented in Python. The game offers multiple features that make it more engaging and interactive. These features include a single-player mode with an AI opponent, time-limited moves, the ability to undo the last move, a customizable board size, and visually enhanced output using colored text.

## Features

- **Single-player Mode**: Play against an AI opponent with a strategic move system where the AI can either block your winning moves or try to win itself.
- **Two-player Mode**: Play with a friend locally.
- **Time-limited Moves**: Each player has a set amount of time to make their move. If the time limit is exceeded, the player's turn is skipped.
- **Undo Move**: Players can undo their previous move if desired, allowing for dynamic and strategic gameplay.
- **Customizable Board Size**: The game allows players to choose the size of the board, such as a 3x3, 4x4, or even larger grids.
- **Colored Output**: Moves are color-coded using the `colorama` library:
  - 'X' moves are displayed in **red**.
  - 'O' moves are displayed in **blue**.
  - Winning positions are highlighted in **green** to indicate the winning combination.
- **Score Tracking**: The game keeps track of the score for each player and displays it after every round.
- **Replay Option**: At the end of each game, players can choose to play again or exit.

## Requirements

- Python 3.x
- `colorama` library for colored text output (install using `pip install colorama`)

## Game Flow

The game follows a simple flow:

1. **Board Setup**: The player chooses the size of the board (minimum 3x3).
2. **Player Choice**: Each player chooses their symbol (default 'X' for Player 1 and 'O' for Player 2).
3. **Mode Selection**: The player selects between single-player (AI) or two-player mode.
4. **Turn-Based Gameplay**: Players alternate turns, and each player has a set time limit to make their move. The game checks after each move to determine if there's a winner or a draw.
5. **AI Opponent (Single-player Mode)**: The AI either blocks the player's winning move or tries to win itself. If there is no immediate threat, the AI makes a random move.
6. **Undo Move**: After a move, players are prompted if they wish to undo their last move. This option can help players if they make a mistake.
7. **Winning Condition**: The game checks if any row, column, or diagonal has all the same symbols (either 'X' or 'O'). If so, the game announces the winner.
8. **Draw Condition**: If the board is full and there is no winner, the game announces a draw.
9. **Game Replay**: After each round, players can choose to play again or exit the game. The score is displayed after each game.

## How to Play

1. **Start the game**: Run the Python script.
2. **Select Board Size**: Enter the size of the board (e.g., 3 for 3x3, 4 for 4x4, etc.).
3. **Choose Player Symbols**: Player 1 (X) and Player 2 (O) can customize their symbols.
4. **Select Game Mode**: Choose between single-player (against AI) or two-player mode.
5. **Set Time Limit**: Enter the time limit for each move (in seconds).
6. **Make Moves**: Players take turns entering their move, selecting a position on the board (e.g., 1-9 for a 3x3 grid).
7. **Undo Move**: If needed, players can undo their last move by typing "yes" when prompted.
8. **Winning/Draw**: The game announces a winner if there’s one, or a draw if no winner is found.

## Code Explanation

The code is divided into several functions that handle specific aspects of the game:

1. **print_board(board, winning_positions=None)**: This function prints the Tic Tac Toe board and highlights the winning positions if available. It uses `colorama` to color the 'X' and 'O' moves in red and blue, respectively, and highlights the winning positions in green.

2. **check_win(board)**: This function checks if a player has won by examining the rows, columns, and diagonals. It returns the winner ('X' or 'O') and the winning positions or None if no winner is found.

3. **is_draw(board)**: This function checks if the game is a draw by ensuring there are no empty spaces left on the board and there is no winner.

4. **player_move(board, current_player, time_limit)**: This function handles the player's move, checks if the move is valid, and ensures that the player stays within the time limit. If the player takes too long, their turn is skipped.

5. **ai_move(board)**: This function handles the AI's move. It first checks if the AI can win or block the player. If neither is possible, the AI chooses a random empty cell.

6. **tic_tac_toe()**: This is the main function that controls the flow of the game. It initializes the board, sets up the game mode, and alternates turns between the players (and the AI in single-player mode). It also handles the replay feature and score tracking.

## Contributing

If you have suggestions, bug fixes, or improvements for this project, feel free to fork the repository and submit a pull request. Contributions are welcome!

## Acknowledgments

- Thanks to the Python community for providing great libraries and resources.
- Special thanks to the original creators of Tic Tac Toe for making this timeless game.
- Thanks to the contributors of the `colorama` library for making colored text in Python easier.

## Contact

Feel free to reach out to me at [vedant.jadhav1928@gmail.com] for any questions or comments.

