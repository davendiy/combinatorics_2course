#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 23.11.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

""" Testing both recursive and dynamic solution for Matrix Chain problem.
    Generate random sequence and calculate it with brackets from both solutions and
    without them.

    Result of testing is situated in 'output_test.txt', because the program is so slow.
"""


from dz3_matrix_chain.mxchn_recursive import memoized_matrix_chain
from dz3_matrix_chain.mxchn_dynamic import MatrixChainOrder, get_answer
import numpy as np
import random
import time


def crmc(n, max_dimension=1000):
    """ Create random matrix chain for Matrix Chain Multiplication problem

    :param n: number of matrix
    :param max_dimension: obvious
    :return: array of dimensions, list of matrix
    """

    p = [0] * n
    for i in range(n):           # generate sequence of dimensions less than max_dimension
        p[i] = random.randrange(max_dimension)

    matrix_list = []
    for i in range(1, n):                        # generate n matrix with generated dimensions
        tmp = np.zeros((p[i-1], p[i]))
        for j in range(p[i-1]):
            for k in range(p[i]):
                tmp[j, k] = random.randrange(100)
        matrix_list.append(np.matrix(tmp))       # not array because matrix multiplication != array multiplication

    return p, matrix_list


def multiplication(answer, matrix_list):
    """ Transform answer from testing program into
        correct python expression and calculate it then

    :param answer: array of string from set {'(', ')', 'a[i]'}
    :param matrix_list: list of matrix that we will calculate
    :return: correct python expression, product
    """
    expression = ''
    flag = True         # True if the previous symbol was 'a[i]' or ')', so we need write '*' after it

    for el in answer:
        if el == '(' and flag:     # so many variants
            expression += ' * ('
            flag = False
        elif el == '(':
            expression += '('
        elif el == ')':
            expression += ')'
            flag = True
        elif flag:
            expression += ' * ' + el
        else:
            expression += el
            flag = True

    expression = expression.strip(' * ')         # delete the first and the last '*'
    t = time.time()
    res = eval(expression, {'a': matrix_list})   # compile right python expression like standard piece of program

    print('time for multiplication with brackets: {}'.format(time.time() - t))    # print elapsed time
    return expression, res


if __name__ == '__main__':
    length = 100                   # length of test sequence
    test_p, test_matrix = crmc(100)
    print("generated sequence of matrix has array of dimensions {}".format(test_p))
    print("length of sequence: {}".format(length))

    # a little bit of pretty print
    print('\n\n=====================recursive method============================')
    res_m1, s = memoized_matrix_chain(test_p)
    answer1 = []
    get_answer(s, 1, length - 1, answer1)

    print("maximum number of operations: {}".format(res_m1[1][length - 1]))
    answer_seq, product = multiplication(answer1, test_matrix)
    print('sequence with brackets: {}'.format(answer_seq))

    print('\n\n======================dynamic method=============================')
    res_m2, s = MatrixChainOrder(test_p, length)
    answer2 = []
    get_answer(s, 1, length - 1, answer2)

    print("maximum number of operations: {}".format(res_m2[1][length - 1]))
    answer_seq, product2 = multiplication(answer2, test_matrix)
    print('sequence with brackets: {}'.format(answer_seq))

    print('\n\n==================direct multiplication===========================')
    string = '*'.join(('test_matrix[{}]'.format(index) for index in range(length - 1)))

    test_time = time.time()               # calculate matrix multiplication directly, like in
    eval(string, {'test_matrix': test_matrix})     # function 'multiplication'
    print("time elapsed: {}".format(time.time() - test_time))
