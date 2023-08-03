#!/usr/bin/python3
"""
program that solves the N queens problem
Usage: nqueens N
    If the user called the program with the wrong
    number of arguments, print Usage: nqueens N,
    followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number,
    followed by a new line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4,
    followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
    One solution per line
    Format: see example
    You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
"""


import sys


def generate_solutions(row, column):
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():

    n = init()
    # generate all solutions
    solutions = generate_solutions(n, n)
    # print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
