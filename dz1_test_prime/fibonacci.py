#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 23.11.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com


import time


def fib_recursive(n, memo):
    if n in [0, 1]:
        return 1

    elif n in memo:
        return memo[n]

    else:
        tmp = fib_recursive(n-1, memo) + fib_recursive(n-2, memo)
        memo[n] = tmp
        return tmp


def dp_fib(n):
    res = [0] * (n+1)
    res[0], res[1] = 1, 1
    for i in range(2, n+1):
        res[i] = res[i-1] + res[i-2]
    return res


def fib(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b


if __name__ == '__main__':
    t = time.time()
    res1 = {}
    test_n = 1000000
    print(f'n = {test_n}')
    print('=============recursive===========')
    try:
        fib_recursive(test_n, res1)
        print('time elapsed: {}'.format(time.time() - t))
        # for el in sorted(res1.keys()):
        #     print(res1[el], end=' ')
    except RecursionError:
        print('recursive error')

    t = time.time()
    res2 = fib(test_n)
    print('==============dynamic===========\n'
          'time elapsed: {}'.format(time.time() - t))

    # for el in res2:
    #     print(el, end=' ')
