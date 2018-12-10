#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 10.12.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

import random
from dz6_mst.graph import Graph
from dz6_mst.kruskal import kruskal_algo
from dz6_mst.prim import prim_algo, treeWeight
import time
from copy import deepcopy


def inputGraphWithRandomVertexPositions(graph, vertices, edges):
    """ Ініціалізація графу випадковим чином.

    Заповнює граф вершинами з випадковими позиціями та ребрами з випадковою вагою

    :param graph: Порожній граф
    :param vertices: Кількість вершин
    :param edges: Кількість ребер
    :return: None
    """

    for v in range(vertices + 1):
        graph.add_vertex(v)

        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        pos = (x, y)
        graph.set_data(v, pos)

    for e in range(edges):
        frm = random.randint(0, vertices)
        to = random.randint(0, vertices)
        if frm != to:
            graph.add_edge(frm, to)


if __name__ == '__main__':
    test = Graph()
    n = 100
    m = random.randrange(n, 200)
    inputGraphWithRandomVertexPositions(test, n, m)
    print(f'n = {n}, m = {m}')
    test2 = deepcopy(test)
    print(test)

    print('\n\nby prim algorithm')
    t = time.time()
    rez = prim_algo(test)
    print(rez)
    print(treeWeight(rez))
    print('time elapsed: {}'.format(time.time() - t))

    print('\n\nby kruskal algorithm')
    t = time.time()
    rez = kruskal_algo(test2)
    print(rez)
    print(treeWeight(rez))
    print('time elapsed: {}'.format(time.time() - t))
