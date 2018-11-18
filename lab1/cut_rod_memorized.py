#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkol
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

import random


def CUTROD(p, n, memo):
    if memo[n] >= 0:
        return memo[n]
    if n == 0:
        q = 0
    else:
        q = -100
        for i in range(1, n + 1):
            q = max(q, p[i] + CUTROD(p, n - i, memo))
    memo[n] = q
    return q


size = 800
valueList = sorted([random.randrange(size * 10) for j in range(size + 1)])
memo = [-1 for k in range(size + 1)]

x = CUTROD(valueList, size, memo)
print("The optimal solution is:")
print(x)
