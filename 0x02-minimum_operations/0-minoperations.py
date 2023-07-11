#!/usr/bin/python3

"""
contains function minOperations(n)
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters
    """
    if n <= 1:
        return 0

    operations = 2  # Start with Copy All and Paste
    h_count = 1  # Initial character H

    while h_count < n:
        if n % h_count == 0:
            operations += 1  # Perform Paste operation
            h_count *= 2
        else:
            operations += 2  # Perform Copy All and Paste operations
            h_count += h_count

    return operations
