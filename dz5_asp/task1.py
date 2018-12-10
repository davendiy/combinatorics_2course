#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 07.12.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

"""The following implementation assumes that the activities
are already sorted according to their finish time
"""

import random
import time
import functools


def cache(func):
    """ Decorator for save answers of any function
    """
    results = {}

    @functools.wraps(func)
    def __cache(*args):         # changed function
        nonlocal results               # if this function call with parameters that already used
        if args in results.keys():     # then answer gets from dictionary
            # print("{} - got from cache".format(args))
            rez = results[args]
        else:
            rez = func(*args)
            results[args] = rez
        return rez

    return __cache


def recursive(s, f):
    s = tuple([0] + s + [1000050000])
    f = tuple([0] + f + [1000050000])
    n = len(f)
    return _recursive(s, f, 0, n-1)


@cache
def _recursive(func_s, func_f, i, j):
    _max = 0
    for k in range(i, j+1):
        if func_f[i] <= func_s[k] < func_f[k] <= func_s[j]:
            tmp_max = _recursive(func_s, func_f, i, k) + _recursive(func_s, func_f, k, j) + 1
            if tmp_max > _max:
                _max = tmp_max
    return _max


def dynamic(s, f):
    """ Dynamic solution of ASP problem. Using recurrent formula
    from Kormen.

    :param s: An array that contains start time of all activities
    :param f: An array that contains finish time of all activities
    :return: optimal sequence of indexes
    """
    n = len(s)
    func_s = [0] + s + [10005000]   # adding to arrays of activities a fictive elements
    func_f = [0] + f + [10005000]
    dp = [[0 for i in range(n+2)] for i in range(n+2)]   # dp[i][j] is max activities from i to j

    for i in range(n+2):
        for j in range(n+2):       # fills all positions in dynamic table
            _max = 0
            for k in range(i, j+1):   # go through all activities that might be done between i-th and j-th
                if func_f[i] <= func_s[k] < func_f[k] <= func_s[j]:
                    tmp_max = dp[i][k] + dp[k][j] + 1    # find maximum
                    if tmp_max > _max:
                        _max = tmp_max
            dp[i][j] = _max
    return dp[0][n+1]


def printMaxActivities(s, f):
    """Prints a maximum set of activities that can be done by a
    single person, one at a time

    :param s: An array that contains start time of all activities
    :param f: An array that contains finish time of all activities
    :return: optimal sequence of indexes
    """
    n = len(f)
    print("The following activities are selected")

    # The first activity is always selected
    i = 0
    print(i, end=' ')

    # Consider rest of the activities
    for j in range(1, n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print(j, end=' ')
            i = j


# Driver program to test above functions

if __name__ == '__main__':
    test_s = []
    test_f = []
    test = []

    N = 1000
    for count in range(N):
        tmp_s = random.randrange(1, N)
        tmp_f = random.randrange(tmp_s+1, N+1)
        test.append((tmp_f, tmp_s))

    test.sort()
    for el in test:
        test_s.append(el[1])
        test_f.append(el[0])

    print(test_s)
    print(test_f)

    print(f"n == {N}")

    print('\n=====by greedy=====')
    t = time.time()
    print('result:')
    printMaxActivities(test_s, test_f)
    print('\ntime elapsed: {}'.format(time.time() - t))

    print('\n=====by dynamic=====')
    t = time.time()
    print('result:\n{}'.format(dynamic(test_s, test_f)))
    print('time elapsed: {}'.format(time.time() - t))

    # print('\n===by recursive===')
    # print(recursive(test_s, test_f))
