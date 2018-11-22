#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 22.11.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

""" Recursive solution for reversed Matrix Chain Multiplication problem
    with building the right sequence of matrix and brackets.
"""

import time

MIN = int(1e+10)


def memoized_matrix_chain(p):
    """ Cover for recursive function _lookup_chain

    :param p: array of dimensions of matrix
    :return: array n x n of maximum amount of elementary operations for each pair i, j
             array n x n of right split of matrix chain
    """
    n = len(p) - 1
    m = {}
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            m[i][j] = MIN
    _lookup_chain(m, p, 1, n)
    return m


def _lookup_chain(m, p, i, j):
    if m[i][j] < MIN:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = _lookup_chain(m, p, i, k) + _lookup_chain(m, p, k + 1, j) + p[i - 1] * p[k] * p[j]
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
