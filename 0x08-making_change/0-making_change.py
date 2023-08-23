#!/usr/bin/python3

"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total amount.
    """
    if total <= 0:
        return 0

    # array dp to store the minimum coins needed for each amount from 0 - total
    dp = [float('inf')] * (total + 1) # all elements set to positive infinity
    dp[0] = 0 # we need 0 coins to make change for 0 amount

    # Loop through each possible amount up to the target total
    for amount in range(1, total + 1):
        # Check each coin denomination
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still float('inf'), it means we couldn't make change for the total
    if dp[total] == float('inf'):
        return -1
    
    return dp[total]
