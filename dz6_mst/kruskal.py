#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 10.12.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

from dz6_mst.graph import Graph
from dz6_mst.disjoint_sets import DisjointSets


def kruskal_algo(graph: Graph):
    pre_sort = {}  # graph is non-oriented, so edges dict contains of keys (2, 3) and (3, 2) are always
    for k, v in graph.edges.items():
        if v not in pre_sort.keys():
            pre_sort[v] = k
    sorted_edges = sorted(pre_sort.items())
    ds = DisjointSets(graph.mVertices.keys())
    tree = Graph(graph.mVertices.keys())
    for weight, nodes in sorted_edges:
        if ds.is_full():
            break
        if not ds.is_same_set(nodes[0], nodes[1]):
            tree.add_edge(nodes[0], nodes[1], weight)
            ds.union(nodes[0], nodes[1])
    return tree


if __name__ == '__main__':
    g = Graph(range(1, 6))
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 5, 12)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 6)
    g.add_edge(2, 4, 3)
    g.add_edge(2, 5, 4)
    print(g)
    print(g.edges)
    # t = prim_algo(g, g.get_node(1))
    # print(t._edges)
    print('\n')
    t = kruskal_algo(g)
    print(t.edges)
