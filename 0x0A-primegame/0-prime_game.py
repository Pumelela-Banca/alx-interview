#!/usr/bin/python
"""
prime game file
"""


def isWinner(x, nums):
    """
    prime game function.
    """
    maria_wins = 0
    ben_wins = 0

    for i, n in enumerate(nums, start=1):
        primes = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        primes = [p for p in range(2, n) if primes[p]]
        turn = 0
        while len(primes) > 0:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            turn += 1
        if turn % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
        if i == x:
            break

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
