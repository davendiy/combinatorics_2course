#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com
# 19.11.18


def dynamic(a, b):
    m = len(a)
    n = len(b)
    val = [[0] * n] * m
    for i in range(1, m):
        for j in range(1, n):
            if a[i] == b[j]:
                val[i][j] = val[i-1][j-1] + 1
            else:
                val[i][j] = max(val[i-1][j], val[i][j-1])
    return val


if __name__ == '__main__':
    test_a = 'abcads'
    test_b = 'abcadgfhkgkfgkfgss'
    print(len(test_a))
    print(len(test_b))
    for row in dynamic(test_a, test_b):
        print(row)
