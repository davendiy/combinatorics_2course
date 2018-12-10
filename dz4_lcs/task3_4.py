#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 02.12.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com
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


@cache
def recursive(a: tuple, i: int, j: int):
    """ Recursive solution of the longest monotone subsequence
    :param a: sequence (must be the tuple or any other hashable sequence for cache)
    :param i: right bound
    :param j: left bound
    :return: length of the longest subsequence, subsequence
    """
    if i == j:                 # if right bound == left bound then sequence is one element
        return 1, (a[i], )

    _pre_count, _pre_seq = recursive(a, i-1, j)   # check if a[i] is continuation of previous max sequence
    if a[i] >= _pre_seq[-1]:
        return _pre_count + 1, _pre_seq + (a[i], )
    else:
        max_count = 1
        max_seq = (a[i],)
        for k in range(j, i):          # if it's false - check all sequences between i and j
            tmp_count, tmp_seq = recursive(a, i-1, k)      # from k to i-1
            if tmp_count+1 > max_count and a[i] >= tmp_seq[-1]:   # find maximum
                max_count = tmp_count + 1
                max_seq = tmp_seq + (a[i], )

        for k in range(i):
            tmp_count, tmp_seq = recursive(a, k, 0)   # and between 0 and i
            if tmp_count+1 > max_count and a[i] >= tmp_seq[-1]:    # from 0 to k
                max_count = tmp_count + 1
                max_seq = tmp_seq + (a[i], )

        return (max_count, max_seq) if max_count > _pre_count else (_pre_count, _pre_seq)


def dynamic(a, b):
    """ Dynamic solution for the longest common sequence of
    consecutive numbers

    :param a: sequence of numbers
    :param b: sequence of numbers
    :return: sequenve of numbers
    """
    m = len(a)
    n = len(b)
    d = [[0 for i in range(n)] for j in range(m)]    # d[i][j] is length of common sequence of consecutive
    prev = [-1 for j in range(n)]                    # numbers that ends with a[i] == b[j]
    global_max = 0
    global_pos = -1
    for i in range(0, m):
        for j in range(0, n):        # iterate through all the elements by dual circle
            if a[i] == b[j]:         # if pair is equal then check if there is sequence that ends with a[i]-1
                max_len = 0   # find longest sequence ends with a[i]-1
                max_prev = -1
                for k in range(i+1):
                    for l in range(j+1):
                        if k == i and l == j:
                            continue
                        if d[k][l] > max_len and a[k] == b[l] == a[i] - 1:
                            max_len = d[k][l]
                            max_prev = l
                d[i][j] = max_len + 1
                if d[i][j] > global_max:
                    global_max = d[i][j]
                    global_pos = j
                prev[j] = max_prev

    res = []                   # rebuild the answer
    while global_pos != -1:
        res.append(b[global_pos])
        global_pos = prev[global_pos]

    return res[::-1]


if __name__ == '__main__':
    test_a = [5, 2, 7, 3, 8, 34, 9, 4, 2, 7, 0, 1, 6, 3, 67, 5, 6]
    test_b = [1, 2, 7, 2, 6, 3, 7, 9, 32, 7, 2, 4, 7, 5, 45, 36, 100, 213, 6]
    test_m = len(test_a)
    test_n = len(test_b)

    print(dynamic(test_a, test_b))
    print(dynamic(test_a, test_b))
