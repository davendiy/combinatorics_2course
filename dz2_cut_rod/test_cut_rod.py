#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 22.11.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

"""
test both recursive and dynamic functions

----------------------------------------------Example of result---------------------------------------------------------

size: 100,
cost of cut: 8,
arr: [8, 20, 80, 83, 110, 115, 116, 123, ... , 953, 953, 970, 985, 994, 998]

=========dynamic solution===========
Maximum Obtainable Value is 2379,
Sequence of indexes: [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

=========recursive solution===========
Maximum Obtainable Value is 2379,
Sequence of indexes: [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

"""

import random
from dz2_cut_rod import *

size = 100
cost_cut = random.randrange(size)
test_memo = [-1 for k in range(size+1)]    # cache for recursive solution
test_seq = [[] for k1 in range(size+1)]

arr = sorted([random.randrange(size * 10) for i in range(size)])    # test sequence of prices

res_val, res_seq = cutrod_dynamic(arr, size, cost_cut)      # dynamic solution

# for recursive function we must add zero element to begin of array of prices
res_val2, res_seq2 = cutrod_memorized([0] + arr, size, cost_cut, test_memo, test_seq)

print("size: {}, \ncost of cut: {}, \narr: {}".format(size, cost_cut, arr))

print("\n=========dynamic solution===========")
print("Maximum Obtainable Value is {},\nSequence of indexes: {}".format(res_val, res_seq))

print("\n=========recursive solution===========")
print("Maximum Obtainable Value is {},\nSequence of indexes: {}".format(res_val2, res_seq2))
