def create_board():
    """Create an empty 3x3 Tic-Tac-Toe board."""
    return [" " for _ in range(9)]


def display_board(board):
    """Display the board in the terminal."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()