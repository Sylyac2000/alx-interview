#!/usr/bin/python3
"""
This module solve the Prime Game problem
"""


def premiers(n):
    """Return list of prime numbers between 1 and n inclusive
    """
    prime_list = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime_list.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime_list


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime_list = premiers(nums[i])
        if len(prime_list) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
