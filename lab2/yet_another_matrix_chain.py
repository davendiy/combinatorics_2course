#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

import time


def recursive_matrix_chain(p, i, j):
    if i == j:
        return 0
    m = int(1e+10)
    for k in range(i, j):
        q = recursive_matrix_chain(p, i, k) + recursive_matrix_chain(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        if q < m:
            m = q
    return m


def main():
    p = [30, 35, 15, 5, 10, 20, 25, 5, 16, 34, 28, 19, 66, 34, 78, 55, 23]
    print(recursive_matrix_chain(p, 1, len(p) - 1))


if __name__ == '__main__':
    b = time.time()
    main()

    print('total run time is:', time.time() - b)
