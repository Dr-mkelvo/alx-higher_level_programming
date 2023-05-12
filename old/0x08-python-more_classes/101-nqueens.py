#!/usr/bin/python3
"""Solving the "n-queens puzzle
The goal is to calculate how many different combinations
that the 8 queens can be placed on an 8 by 8 chessboard
In such a way that none are a threat to each other
"""
import sys


def board_init(num):
    """Initialization of a num by num chessboard."""
    my_board = []
    [my_board.append([]) for x in range(num)]
    [row.append(' ') for x in range(num) for row in my_board]
    return (my_board)


def my_copy(my_board):
    """A function which returns a copy of the board which have
    different references from the original copy."""
    if isinstance(my_board, list):
        return list(map(my_copy, my_board))
    return (my_board)


def get_result(my_board):
    """Returns a representation of list of lists
    of a solved chessboard.
    """
    results = []
    for row in range(len(my_board)):
        for col in range(len(my_board)):
            if my_board[row][col] == "Q":
                results.append([row, col])
                break
    return (results)


def capture(my_board, row, col):
    """when a piece makes a capture, an X is immediately
    inserted before the destination
    Args:
        my_board (list):My chessboard.
        row(int): The last row where a queen was last played.
        col(int): The lat column where a queen was last played.
    """

    for column in range(col + 1, len(my_board)):
        my_board[row][column] = "x"

    for column in range(col - 1, -1, -1):
        my_board[row][column] = "x"

    for rows in range(row + 1, len(my_board)):
        my_board[rows][col] = "x"

    for rows in range(row - 1, -1, -1):
        my_board[rows][col] = "x"

    column = col + 1
    for rows in range(row + 1, len(my_board)):
        if column >= len(my_board):
            break
        my_board[rows][column] = "x"
        column += 1

    column = col - 1
    for rows in range(row - 1, -1, -1):
        if column < 0:
            break
        my_board[rows][column]
        column -= 1

    column = col + 1
    for rows in range(row - 1, -1, -1):
        if column >= len(my_board):
            break
        my_board[rows][column] = "x"
        column += 1

    column = col - 1
    for rows in range(row + 1, len(my_board)):
        if column < 0:
            break
        my_board[rows][column] = "x"
        column -= 1


def sol_recursive(my_board, row, queen, solution):
    """Solution :Use recursion
    """
    if queen == len(my_board):
        solution.append(get_result(my_board))
        return (solution)

    for column in range(len(my_board)):
        if my_board[row][column] == " ":
            tmp_board = my_copy(my_board)
            tmp_board[row][column] = "Q"
            capture(tmp_board, row, column)
            solution = sol_recursive(tmp_board, row + 1, queen + 1, solution)

    return (solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    my_board = board_init(int(sys.argv[1]))
    solutions = sol_recursive(my_board, 0, 0, [])
    for solution in solutions:
        print(solution)
