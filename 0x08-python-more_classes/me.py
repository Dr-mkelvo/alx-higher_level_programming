#!/usr/bin/python3

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row[:] for row in board]

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [[r, c] for r, row in enumerate(board) for c, val in enumerate(row) if val == "Q"]

def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    n = len(board)
    for i in range(n):
        if i != row:
            board[i][col] = "x"
        if i != col:
            board[row][i] = "x"
    r, c = row-1, col-1
    while r >= 0 and c >= 0:
        board[r][c] = "x"
        r, c = r-1, c-1
    r, c = row-1, col+1
    while r >= 0 and c < n:
        board[r][c] = "x"
        r, c = r-1, c+1
    r, c = row+1, col-1
    while r < n and c >= 0:
        board[r][c] = "x"
        r, c = r+1, c-1
    r, c = row+1, col+1
    while r < n and c < n:
        board[r][c] = "x"
        r, c = r+1, c+1

def recursive_solve(board, queens=0, solutions=[]):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    n = len(board)
    for r in range(n):
        if board[r][queens] == " ":
            tmp_board = deepcopy(board)
            tmp_board[r][queens] = "Q"
            xout(tmp_board, r, queens)
            solutions = recursive_solve(tmp_board, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = recursive_solve(board)
    for sol in solutions:
        print(sol)
