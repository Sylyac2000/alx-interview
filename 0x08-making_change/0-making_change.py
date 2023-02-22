#!/usr/bin/python3
"""This module is about making changes
"""


def makeChange(coins, total):
    """function return fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    # Initialize the list with infinity for all values except 0
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    # Iterate through the coins and update the list
    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    # If the value at the index total is still infinity, return -1
    if min_coins[total] == float('inf'):
        return -1
    return min_coins[total]
