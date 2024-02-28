#!/usr/bin/python3
"""
function that  fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    given coins how many are needed to make total
    """
    if total <= 0:
        return 0
    left = total
    count = 0
    i = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while left > 0:
        if i >= n:
            return -1
        if left - sorted_coins[i] >= 0:
            left -= sorted_coins[i]
            count += 1
        else:
            i += 1
    return count
