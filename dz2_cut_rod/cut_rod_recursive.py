#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 22.11.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

"""
Recursive solution for Rod cutting problem with cost of cutting
"""

import random


def cutrod_memorized(p, n, cut_cost, memo, res_seq):
    """ Returns the best obtainable price for a rod of length n and
        price[] as prices of different pieces and sequence of
        length of pieces that give the obtainable price.

    :param p: array of prices
    :param n: length of rod
    :param cut_cost: cost of cutting
    :param memo: array of previous returns (cache)
    :param res_seq: array of pieces
    :return: obtainable price, array of pieces
    """
    if memo[n] >= 0:                 # if we have already calculated price for given parameters
        return memo[n], res_seq[n]   # return the calculated result
    if n == 0:
        return 0, 0                  # max income and best piece for rod of zero length
    else:
        max_income = -100
        best_piece = -1
        for i in range(1, n + 1):
            tmp, tmp_seq = cutrod_memorized(p, n - i, cut_cost, memo, res_seq)
            if tmp + p[i] - cut_cost > max_income:
                max_income = tmp + p[i] - cut_cost
                best_piece = i       # in addition remember the piece we used
    memo[n] = max_income
    res_seq[n] = res_seq[n-best_piece] + [best_piece-1]    # update dynamic arrays
    return max_income, res_seq[n]


if __name__ == '__main__':

    # test for above function
    size = 10
    test_cost = random.randrange(size)
    valueList = sorted([random.randrange(size * 10) for j in range(size + 1)])
    test_memo = [-1 for k in range(size + 1)]
    test_seq = [[] for k1 in range(size + 1)]

    x = cutrod_memorized(valueList, size, test_cost, test_memo, test_seq)
    print("The optimal solution is:")
    print(x)
