#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 23.11.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

"""The following implementation assumes that the activities
are already sorted according to their finish time

Prints a maximum set of activities that can be done by a
single person, one at a time"""


# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities

def printMaxActivities(s, f):
    n = len(f)
    print("The following activities are selected")

    # The first activity is always selected
    i = 0
    print(i)

    # Consider rest of the activities
    for j in range(n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print(j)
            i = j


# Driver program to test above function

test_s = [1, 3, 0, 5, 8, 5]
test_f = [2, 4, 6, 7, 9, 9]
printMaxActivities(test_s, test_f)
