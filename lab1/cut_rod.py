#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkol
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

# A Naive recursive solution
# for Rod cutting problem
import sys
import random


def cutRod(price, n):
    """
    Returns the best obtainable price for a rod of length n
    and price[] as prices of different pieces
    """
    if n <= 0:
        return 0
    max_val = -sys.maxsize - 1

    # Recursively cut the rod in different pieces
    # and compare different configurations
    for i in range(0, n):
        max_val = max(max_val, price[i] +
                      cutRod(price, n - i - 1))
    return max_val


# Driver code
size = 24
arr = sorted([random.randrange(size * 10) for j in range(size)])

print("Maximum Obtainable Value is", cutRod(arr, size))
