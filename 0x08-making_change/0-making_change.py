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
    
    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    return count if total == 0 else -1
