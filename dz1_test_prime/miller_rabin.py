#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

"""
Домашнє завдання №1, тест Міллера-Рабіна на простоту
"""

import random


def check(a, s, d, n):
    """
    перевірка одного свідка простоти
    :param a: підозрілий свідок
    :param s: степінь двійки в простому розкладі n
    :param d: добуток простих чисел, відмінних від 2, з простого розкладу n
    :param n: число, яке перевіряється
    :return:
    """
    x = pow(a, d, n)     # піднесення до степеня по модулю
    if x == 1:
        return True
    for i in range(s - 1):      # перевірка тестів
        if x == n - 1:
            return True
        x = pow(x, 2, n)
    return x == n - 1


def miller_rabin_test(n, round_count):
    """ Тест Міллера-Рабіна.

    :param n: число, яке тестується
    :param round_count: к-ть раундів
    :return:
    """
    d = n - 1       # добуток простих дільників n, відмінних від 2
    s = 0           # степінь двійки у простому розкладі n
    while d & 1 == 0:
        d //= 2
        s += 1

    flag = True     # результат теста
    for i in range(round_count):
        # print("test number: {}".format(i))
        a = random.randrange(2, n-1)
        if not check(a, s, d, n):             # якщо знайшли свідка складеності - виходимо з циклу
            flag = False
            break

    return flag


if __name__ == '__main__':
    for number in range(5, 1000):        # перевірка на простоту всіх чисел від 5 до 999
        print("miller test for {}: {}".format(number, miller_rabin_test(number, number)))
