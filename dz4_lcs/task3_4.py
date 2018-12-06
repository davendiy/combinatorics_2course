#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 02.12.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com


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
