#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 22.11.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

""" Dynamic solution for reversed Matrix Chain Multiplication problem
    with building the right sequence of brackets.
"""


def MatrixChainOrder(p, n):
    """ Dynamic Programming Python implementation of Matrix
        Chain Multiplication - build the worst sequence of brackets
        (it means that this sequence have the biggest number of elementary operations).

    :param p: array of dimensions
    :param n: length of matrix sequence
    :return: array n x n of maximum amount of elementary operations for each pair i, j
             array n x n of right split of matrix chain
    """

    # Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[-1 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    # m[i,j] = MNone (array changes inside of function)inimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0

    for length in range(2, n):       # for each chain length
        for i in range(1, n - length + 1):
            j = i + length - 1
            for k in range(i, j):

                # cost = cost/scalar multiplications
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost > m[i][j]:     # find maximum
                    m[i][j] = cost
                    s[i][j] = k        # in addition we remember place, where we did the split

    return m, s


def get_answer(s, i, j, res: list):
    """ Reconstruct the sequence of brackets and matrix
        that give the maximum number of operations

    :param s: array n x n of right split of matrix chain from MatrixChainOrder
    :param i: start of piece
    :param j: end of piece
    :param res: array of string from set {'(', ')', 'a[i]'}
    :return: None (array changes inside of function)
    """
    if i == j:
        res.append('a[{}]'.format(i))    # on the main diagonal length of piece == 0, so matrix only one
    else:
        res.append('(')                  # at the other places the internal block of matrix opens
        get_answer(s, i, s[i][j], res)
        get_answer(s, s[i][j]+1, j, res)
        res.append(')')


if __name__ == '__main__':

    # test of the above function
    arr = [1, 2, 3, 4]
    size = len(arr)
    res_m, res_s = MatrixChainOrder(arr, size)
    answer = []
    get_answer(res_s, 1, size-1, answer)
    print("Minimum number of multiplications is {}".format(res_m[1][size-1]))

    print("The right sequence is {}".format(answer))
