#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


def main():
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

    board = [-1] * n
    solutions = []
    solve_nqueens(n, 0, board, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
