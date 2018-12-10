#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 07.12.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com


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


def get_subset(s, f, i, j):
    if i == 0:
        start = 0
    else:
        start = f[i - 1]
    if j == len(s):
        finish = 1 << 20
    else:
        finish = s[j]
    res = [(s[k], f[k]) for k in range(len(s)) if s[k] > start and f[k] < finish]
    return res


def rec(s, f, v, i, j):
    if not get_subset(s, f, i, j):
        return 0
    else:
        vals = [rec(s, f, v, i, k) + rec(s, f, v, k, j) + v[k] for k in range(i + 1, j)]
        return max(vals)


def dynamic(s, f, v):
    vals = [[None for a in range(len(s))] for b in range(len(s))]
    indxs = [[None for a in range(len(s))] for b in range(len(s))]
    for a in range(len(s)):
        vals[a][a] = 0
    for c1 in range(1, len(vals)):
        for c2 in range(c1, len(vals)):
            i, j = c2 - c1, c2
            mx = 0
            kx = -1
            for k in range(i + 1, j):
                if get_subset(s, f, i, j):
                    tmp = vals[i][k] + vals[k][j] + v[k]
                    if tmp > mx:
                        mx = tmp
                        kx = k
            vals[i][j] = mx
            indxs[i][j] = kx
    return vals, indxs


def get_res(indxs, i, j):
    if indxs[i][j] == -1 or indxs[i][j] is None:
        return ''
    else:
        k = indxs[i][j]
        return get_res(indxs, i, k) + ' ' +  str(k) + ' ' + get_res(indxs, k, j)


if __name__ == '__main__':
    from random import randrange as rand
    # s = [1, 3, 0, 5, 3, 5]
    # f = [4, 5, 6, 7, 9, 9]
    # v = [rand(1, 30) for i in range(len(s))]
    test_s = [0, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6]
    test_f = [2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8]
    v = [3, 4, 4, 4, 4, 2, 4, 4, 4, 4, 3]
    print(v, end='\n\n')
    r1, r2 = dynamic(test_s, test_f, v)
    print(get_res(r2, 0, len(test_s) - 1))

    printMaxActivities(test_s, test_f)
