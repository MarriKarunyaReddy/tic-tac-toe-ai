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


def make_move(board):
    """Allow the player to place X on an empty cell."""

    while True:
        try:
            position = int(input("Enter your position (0-8): "))

            if position < 0 or position > 8:
                print("Invalid position! Choose a number from 0 to 8.")
            elif board[position] != " ":
                print("That position is occupied! Choose another.")
            else:
                board[position] = "X"
                break

        except ValueError:
            print("Invalid input! Please enter a number.")