#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 10.12.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com


class DisjointSets:
    """ Data structure, represented as a list of disjoint sets,
    any item from a set is considered as it's representative
    """

    def __init__(self, iterable):
        self._data = [{item} for item in iterable]   # init structure with a single-item sets

    def is_full(self):
        """ If list contains only one set it means
        that all union operations had already been performed

        :return: bool
        """
        return len(self._data) == 1

    def add_set(self, repres):
        """ Appends a new set with initial representative "repres"

        :param repres: initial representative
        """
        s = self.set_indx(repres)
        if not s is None:
            raise Exception
        self._data.append(set(repres))

    def is_same_set(self, item1, item2):
        """ Checks if two items belongs to the same set

        :return: bool
        """
        res = False
        for s in self._data:
            if item1 in s and item2 in s:
                res = True
                break
        return res

    def set_indx(self, item):
        """ Searches for set by it's representative
        :param item: representative
        :return: set index in initial list or None if latter was not found
        """
        for i, s in enumerate(self._data):
            if item in s:
                return i
        return None

    def union(self, repres1, repres2):
        if self.is_same_set(repres1, repres2):
            raise Exception
        i1 = self.set_indx(repres1)
        i2 = self.set_indx(repres2)
        set1 = self._data[i1]
        set2 = self._data[i2]
        self._data.remove(set1)
        self._data.remove(set2)
        self._data.append(set1.union(set2))
