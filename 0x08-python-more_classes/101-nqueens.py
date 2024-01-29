#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n):
    if col == n:
        # All queens are placed successfully
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place queen

            # Recur to place rest of the queens
            res = solve_nqueens_util(board, col + 1, n) or res

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove the queen from board[i][col]
            board[i][col] = 0

    return res

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_nqueens_util(board, 0, n):
        print("No solution exists")

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        solve_nqueens(n)

    except ValueError:
        print("N must be a number")
        sys.exit(1)

if __name__ == "__main__":
    main()
