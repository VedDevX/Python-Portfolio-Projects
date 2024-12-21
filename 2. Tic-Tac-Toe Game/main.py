import random  # This imports the random module, which we will use for making random choices in the game (for the AI's move).
import time  # This imports the time module, which allows us to set a time limit for the player's move.
from colorama import Fore, Style  # This imports the colorama module, which helps in adding colors to text (like red, blue, green).

def print_board(board, winning_positions=None):
    """
    This function prints the Tic Tac Toe board.
    It also highlights the winning positions if provided.
    """
    size = len(board)  # We get the size of the board (like 3 for a 3x3 board).
    for r, row in enumerate(board):  # Loop over each row (r is the row index).
        for c, cell in enumerate(row):  # Loop over each cell in the row (c is the column index).
            if winning_positions and (r, c) in winning_positions:
                # If there are winning positions, highlight the cells in green.
                print(Fore.GREEN + cell + Style.RESET_ALL, end=" | ")
            elif cell == 'X':
                # If the cell contains 'X', print it in red color.
                print(Fore.RED + cell + Style.RESET_ALL, end=" | ")
            elif cell == 'O':
                # If the cell contains 'O', print it in blue color.
                print(Fore.BLUE + cell + Style.RESET_ALL, end=" | ")
            else:
                # If the cell is empty (contains ' '), print it normally.
                print(cell, end=" | ")
        print("\n" + "-" * (size * 4))  # Print a separator line after each row to make the board look nice.

def check_win(board):
    """
    This function checks if there is a winner.
    It returns the symbol of the winner ('X' or 'O') and the winning positions, or None if no winner.
    """
    size = len(board)  # Get the size of the board (3 for a 3x3 board).

    # Check rows and columns for a winner.
    for i in range(size):
        if all(board[i][j] == board[i][0] != ' ' for j in range(size)):
            # If all cells in the row i are the same and not empty, then return the winner and the winning positions.
            return board[i][0], [(i, j) for j in range(size)]
        if all(board[j][i] == board[0][i] != ' ' for j in range(size)):
            # If all cells in the column i are the same and not empty, return the winner and the winning positions.
            return board[0][i], [(j, i) for j in range(size)]

    # Check diagonals for a winner.
    if all(board[i][i] == board[0][0] != ' ' for i in range(size)):
        # If all cells in the main diagonal are the same and not empty, return the winner and the winning positions.
        return board[0][0], [(i, i) for i in range(size)]
    if all(board[i][size - i - 1] == board[0][size - 1] != ' ' for i in range(size)):
        # If all cells in the anti-diagonal are the same and not empty, return the winner and the winning positions.
        return board[0][size - 1], [(i, size - i - 1) for i in range(size)]

    return None, []  # If no winner, return None.

def is_draw(board):
    """
    This function checks if the game is a draw (i.e., no empty spaces left and no winner).
    """
    return all(cell != ' ' for row in board for cell in row)  # If there are no empty cells, it's a draw.

def player_move(board, current_player, time_limit):
    """
    This function handles the player's move. It also includes a time limit for the move.
    """
    start_time = time.time()  # Get the current time when the player starts their move.
    while True:
        try:
            # Ask the player to input their move (a number from 1 to size*size).
            move = int(input(f"Player {current_player}, enter your move (1-{len(board)**2}): ")) - 1
            row, col = divmod(move, len(board))  # Convert the move number into row and column.

            if time.time() - start_time > time_limit:  # Check if the player took too long.
                print("Time's up! You lost your turn.")  # If the time is up, the turn is lost.
                return None, None
            if move < 0 or move >= len(board)**2 or board[row][col] != ' ':
                # If the move is invalid (out of bounds or the cell is already taken), ask the player to try again.
                print("Invalid move. Try again.")
                continue
            return row, col  # Return the row and column where the player wants to make their move.
        except (ValueError, IndexError):
            print("Invalid input. Enter a valid number.")  # Handle invalid input.

def ai_move(board):
    """
    This function handles the AI's move. It tries to block the player or win.
    """
    size = len(board)  # Get the size of the board.

    # Check if AI can win
    for r in range(size):
        for c in range(size):
            if board[r][c] == ' ':
                board[r][c] = 'O'  # Temporarily make the move for AI.
                winner, _ = check_win(board)  # Check if AI wins.
                board[r][c] = ' '  # Undo the move.
                if winner == 'O':  # If AI wins, return the move.
                    return r, c

    # Check if AI can block the player
    for r in range(size):
        for c in range(size):
            if board[r][c] == ' ':
                board[r][c] = 'X'  # Temporarily make the move for the player.
                winner, _ = check_win(board)  # Check if the player wins.
                board[r][c] = ' '  # Undo the move.
                if winner == 'X':  # If the player wins, block the move.
                    return r, c

    # Otherwise, make a random move
    empty_cells = [(r, c) for r in range(size) for c in range(size) if board[r][c] == ' ']
    return random.choice(empty_cells)  # If there's no immediate threat, pick a random empty cell.

def tic_tac_toe():
    """
    This function runs the Tic Tac Toe game.
    It handles the game flow, player input, and checking for a winner.
    """
    print("Welcome to Advanced Tic Tac Toe!")  # Display the game welcome message.

    # Ask the player to input the size of the board (e.g., 3 for 3x3).
    while True:
        try:
            size = int(input("Enter the board size (e.g., 3 for 3x3): "))  # Get the board size from the player.
            if size < 3:
                print("Board size must be at least 3. Try again.")  # If the size is less than 3, ask again.
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle invalid input (non-number).

    # Initialize the board with empty spaces.
    board = [[' ' for _ in range(size)] for _ in range(size)]
    scores = {'X': 0, 'O': 0}  # Initialize the scores dictionary for both players.

    # Ask each player to choose their symbol.
    symbol_x = input("Player X, choose your symbol (default 'X'): ") or 'X'
    symbol_o = input("Player O, choose your symbol (default 'O'): ") or 'O'

    # Ask the player to choose the game mode (single-player or two-player).
    mode = input("Enter '1' for single-player or '2' for two-player mode: ").strip()
    while mode not in ['1', '2']:  # Keep asking until a valid input is provided.
        mode = input("Invalid choice. Enter '1' for single-player or '2' for two-player mode: ").strip()

    # Ask the player to set a time limit for each move.
    time_limit = int(input("Enter the time limit for moves (in seconds): "))

    # Main game loop
    while True:
        current_player = symbol_x  # Player X always starts first.
        print_board(board)  # Display the board at the start of each round.

        # Track the last move made for undo feature.
        last_move = None

        while True:
            if mode == '1' and current_player == symbol_o:  # If it's AI's turn in single-player mode.
                print("AI is making its move...")  # Let the player know it's AI's turn.
                row, col = ai_move(board)  # Get AI's move.
            else:  # If it's the player's turn.
                print(f"You have {time_limit} seconds to make a move.")  # Notify the player of the time limit.
                row, col = player_move(board, current_player, time_limit)  # Get the player's move.
                if row is None:  # If the player took too long, skip their turn.
                    current_player = symbol_o if current_player == symbol_x else symbol_x
                    continue
                if input("Do you want to undo your last move? (yes/no): ").lower() == "yes" and last_move:
                    # If the player wants to undo the last move, do it.
                    board[last_move[0]][last_move[1]] = ' '
                    print("Last move undone.")
                    continue
                last_move = (row, col)  # Update the last move.

            # Update the board with the player's or AI's move.
            board[row][col] = current_player
            print_board(board)  # Display the updated board.

            # Check if there's a winner.
            winner, positions = check_win(board)
            if winner:
                print_board(board, positions)  # Highlight the winning positions.
                print(f"Player {winner} wins!")  # Announce the winner.
                scores[winner] += 1  # Update the score of the winner.
                break

            # Check if it's a draw (no winner).
            if is_draw(board):
                print("It's a draw!")  # Announce the draw.
                break

            # Switch turns.
            current_player = symbol_o if current_player == symbol_x else symbol_x

        # Display the scores.
        print(f"Scores: {symbol_x} = {scores[symbol_x]}, {symbol_o} = {scores[symbol_o]}")

        # Ask if the players want to play again.
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Final scores:")
            print(f"{symbol_x} = {scores[symbol_x]}, {symbol_o} = {scores[symbol_o]}")
            break  # End the game.

        # Reset the board for a new game.
        board = [[' ' for _ in range(size)] for _ in range(size)]

# Run the game.
if __name__ == "__main__":
    tic_tac_toe()  # Start the game when the script is run.
