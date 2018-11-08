#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

import random


def ferma_test(n, test_count):
    flag = True
    for i in range(test_count):
        a = random.randrange(2, n - 1)
        if pow(a, n-1, n) != 1:
            flag = False
            break

    return flag


if __name__ == '__main__':
    for number in range(4, 1000):
        print("test for number {}: {}".format(number, ferma_test(number, number)))
