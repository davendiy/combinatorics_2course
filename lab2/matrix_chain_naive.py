#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

# A naive recursive implementation that
# simply follows the above optimal
# substructure property
import sys


# Matrix A[i] has dimension p[i-1] x p[i]
# for i = 1..n
def matrix_chain_order(p, i, j):
    if i == j:
        return 0

    _min = sys.maxsize

    # place parenthesis at different places
    # between first and last matrix,
    # recursively calculate count of
    # multiplications for each parenthesis
    # placement and return the minimum count
    for k in range(i, j):

        count = (matrix_chain_order(p, i, k)
                 + matrix_chain_order(p, k + 1, j)
                 + p[i - 1] * p[k] * p[j])

        if count < _min:
            _min = count
            # Return minimum count
    return _min


# test of the above function
arr = [30, 35, 15, 5, 10, 20, 25, 5, 16, 34, 28, 19, 66, 34, 78, 55, 23]
n = len(arr)

print("Minimum number of multiplications is ",
      matrix_chain_order(arr, 1, n - 1))
