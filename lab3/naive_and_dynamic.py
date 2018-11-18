#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com


def lcs(a, b, i, j):

    if i <= 0 or j <= 0:
        return 0
    elif a[i-1] == b[j-1]:
        return lcs(a, b, i-1, j-1) + 1
    else:
        return max(lcs(a, b, i, j-1), lcs(a, b, i-1, j))


def dynamic(a, b):
    m = len(a)
    n = len(b)
    val = [[0] * n] * m
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                continue
            if a[i] == b[j]:
                val[i][j] = val[i-1][j-1] + 1
            else:
                val[i][j] = max(val[i-1][j], val[i][j-1])
    return val[m-1][n-1] + 1


if __name__ == '__main__':
    test_a = 'abdkjlkjhcacba'
    test_b = 'backjhdl;kba'
    print(len(test_a))
    print(len(test_b))
    print(dynamic(test_a, test_b))
    print(lcs(test_a, test_b, len(test_a), len(test_b)))
