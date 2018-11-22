#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkol
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

""" A Dynamic Programming solution for Rod cutting problem with cost of cutting

"""

import random

INT_MIN = -32767


def cutrod_dynamic(price, n, cut_cost):
    """ Returns the best obtainable price for a rod of length n and
        price[] as prices of different pieces

    :param price: array of prices of rod pieces (price[i] - price of piece of length i)
    :param n: length of rod
    :param cut_cost: cost of cutting
    :return: max price, sequence of indexes
    """
    val = [0] * (n + 1)        # dynamic array of max prices
    seq = [[]] * (n + 1)       # dynamic array of sequences
    val[0] = 0

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        max_val = INT_MIN

        tmp_j = 0
        for j in range(i):
            tmp = price[j] + val[i - j - 1] - cut_cost     # calculating revenue with cost of cutting
            if tmp > max_val:
                max_val = tmp           # memorize revenue and length of rod piece we used
                tmp_j = j
        seq[i] = seq[i - tmp_j - 1] + [tmp_j]    # update dynamic array
        val[i] = max_val

    return val[n], seq[n]


if __name__ == '__main__':
    # Driver program to test above functions
    size = 10
    cost_cut = random.randrange(size)

    arr = sorted([random.randrange(size * 10) for i in range(size)])
    res_val, res_seq = cutrod_dynamic(arr, size, cost_cut)
    print("size: {}, \ncost of cut: {}, \narr: {}".format(size, cost_cut, arr))
    print("Maximum Obtainable Value is {},\nSequence of indexes: {}".format(res_val, res_seq))

    test = 0
    length = 0
    for index in res_seq:
        test += arr[index] - cost_cut
        length += index + 1

    print("test value: {}".format(test))
    print("test length: {}".format(length))
