#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.12.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

from dz6_mst.priority_queue import *
from dz6_mst.graph import Graph

INF = float('inf')


def prim_algo(graph: Graph):
    """ Реалізує алгоритм Пріма побудови каркасного дерева

    :param graph: заданий граф на базі якого будується каркасне дерево
    :return: граф, що є мінімальним каркасним деревом для заданого графа
    """

    assert not graph.mIsOriented
    start = 0  # Вибираємо довільну точку графа як початкову з якої стартує алгоритм

    for vertex in graph:
        vertex.set_distance(INF)
        vertex.set_source(None)  # Вершина з якої прийшли по найкорошому шляху невизначена

    graph[start].set_distance(0)

    pq = PriorityQueue()  # Створюємо пріоритетну чергу

    # Додаємо у чергу з пріоритетом всі вершини графа.
    for vertex in graph:
        pq.insert(vertex.key(), vertex.distance())  # де пріоритет - це відстань у вершині

    while not pq.empty():

        vertex_key = pq.extractMinimum()  # Беремо індекс вершини з черги з найнижчим пріоритетом
        vertex = graph[vertex_key]  # Беремо вершину за індексом

        for neighbor_key in vertex.neighbors():  # Для всіх сусідів (за ключами) поточної вершини
            neighbour = graph[neighbor_key]  # Беремо вершину-сусіда за індексом
            newDist = vertex.weight(neighbor_key)  # Визначаємо вагу ребра між вершиною та вершиною-сусідом

            # Якщо вершина-сусід ще не додана до каркасного дерева і
            # потенційна відстань у вершині-сусіді менша за її поточне значення
            if neighbor_key in pq and newDist < neighbour.distance():
                neighbour.set_distance(newDist)  # Змінюємо поточне значення відстані у вершині-сусіді обчисленим
                neighbour.set_source(
                    vertex_key)  # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї
                pq.decreasePriority(neighbor_key, newDist)  # перераховуємо її пріоритет в черзі

    # Будуємо граф, що є каркасним деревом
    spanning_tree = Graph()
    for vertex in graph:
        destination = vertex.key()
        source = vertex.source()
        if source is None:
            continue
        weight = vertex.weight(source)
        spanning_tree.add_edge(source, destination, weight)

    return spanning_tree


def __treeWeightHelper(graph, visited, start):
    """ Допоміжний рекурсивний метод, який, використовуючи обхід в глибину,
    визначає вагу заданого каркасного дерева (суму ваг усіх ребер)

    :param graph: Заданий граф
    :param visited: Допоміжний список, i-й елемент якого містить позначку чи була відвідана i-та вершина
    :param start: Вершина з якої відбувається запуск обходу в глибину
    :return: Вагу графа
    """
    res = 0
    visited[start] = True  # Помічаємо стартовий елемент як відвіданий
    # для всіх сусідів стартового елементу
    for neighbour in graph[start].neighbors():
        if not visited[neighbour]:  # які ще не були відвідані
            res += graph[start].weight(neighbour)
            res += __treeWeightHelper(graph, visited, neighbour)

    return res


def treeWeight(graph):
    """ Функція знаходження ваги отриманого дерева

    :param graph: Заданий граф
    :return: Вагу графа
    """
    visited = [False] * len(graph)
    return __treeWeightHelper(graph, visited, 0)


if __name__ == "__main__":   # Для тестування

    g = Graph()

    g.add_edge(0, 1, 7)
    g.add_edge(0, 5, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 4, 3)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 0, 5)
    g.add_edge(5, 4, 2)
    g.add_edge(5, 2, 3)
    g.add_edge(6, 3, 1)
    g.add_edge(6, 2, 1)
    g.add_edge(6, 7, 12)
    g.add_edge(7, 4, 2)

    # t = GraphForAlgorithms()
    t = prim_algo(g)
    print(t)
    print(treeWeight(t))
