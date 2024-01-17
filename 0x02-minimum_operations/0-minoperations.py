#!/usr/bin/python3
"""
minimum operations to get to text
"""


def minOperations(n):
    """
    minimum operations to get to n H's
    """
    if n <= 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n % 2 != 0 and n % 3 != 0:
        return n
    count_half = 0
    new_num = n
    divider = 0
    if n % 2 == 0:
        divider = 2
    elif n % 3 == 0:
        divider = 3
    while True:
        count_half += divider
        new_num = new_num / divider
        if new_num % divider == 0 and new_num != divider:
            continue
        return int(count_half + new_num)
