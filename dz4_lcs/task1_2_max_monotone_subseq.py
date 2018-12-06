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


def dynamic(a):
    """ Dynamic solution of the longest monotone subsequence
    :param a: sequence
    :return: the longest subsequence and its length
    """
    n = len(a)
    dyn = [1 for i in range(n)]      # dyn[i] is longest subseq from 0 to i
    res_array = [-1 for i in range(n)]    # res_array[i] is index of choice in i-th problem
    for i in range(n):
        for j in range(i):           # on the i-th iteration we must choose the maximum subsequence
            if a[j] <= a[i]:         # with all the elements lower than a[i] from all previous answers
                if 1 + dyn[j] > dyn[i]:
                    dyn[i] = 1 + dyn[j]
                    res_array[i] = j
    pos = -1
    res = 0
    for i, el in enumerate(dyn):   # find longest from all answers
        if el > res:
            res = el
            pos = i

    path = []
    while pos != -1:               # rebuild the sequence
        path.append(a[pos])
        pos = res_array[pos]
    return res, path[::-1]


if __name__ == '__main__':
    test_a = (2, 10, 9, 8, 8, 10, 5, 7, 6, 11, 32, 2, 2, 32, 44)
    test_n = len(test_a)
    print(*recursive(test_a, test_n - 1, 0))

    print(*dynamic(test_a))
