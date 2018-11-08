#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

"""
Домашнє завдання №1, тест Ферма на простоту
"""

import random


def ferma_test(n: int, test_count: int) -> bool:
    """ Тест простоти Ферма.

    :param n: число, яке перевіряється
    :param test_count: к-ть тестів
    :return: True - вірогідно просте, False - складене
    """
    flag = True
    for i in range(test_count):
        a = random.randrange(2, n - 1)      # генеруємо рандомне число
        if pow(a, n-1, n) != 1:             # підносимо до степеня і перевіряємо
            flag = False
            break

    return flag


if __name__ == '__main__':
    for number in range(4, 1000):
        print("test for number {}: {}".format(number, ferma_test(number, number)))
