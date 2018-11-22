#!/usr/bin/env python3
# -*-encoding: utf-8-*-

import time

MAX = int(1e+10)


def memoized_matrix_chain(p):
    n = len(p) - 1
    m = {}
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            m[i][j] = MAX
    return lookup_chain(m, p, 1, n)


def lookup_chain(m, p, i, j):
    if m[i][j] < MAX:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]


def main():
    p = [30, 35, 15, 5, 10, 20, 25, 5, 16, 34, 28, 19, 66, 34, 78, 55, 23]
    print(memoized_matrix_chain(p))


if __name__ == '__main__':
    b = time.time()
    main()
    print('total run time is:', time.time() - b)
