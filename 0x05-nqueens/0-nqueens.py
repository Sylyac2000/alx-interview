#!/usr/bin/python3
"""This module solves the N queens problem"""

import sys


def solve(row, n, cols, pos, negatif, board):
    """solves the N queens problem"""
    if row == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (row + c) in pos or (row - c) in negatif:
            continue

        cols.add(c)
        pos.add(row + c)
        negatif.add(row - c)
        board[row][c] = 1

        solve(row+1, n, cols, pos, negatif, board)

        cols.remove(c)
        pos.remove(row + c)
        negatif.remove(row - c)
        board[row][c] = 0


def nqueens(n):
    """sets up board and solve"""
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]
    solve(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
