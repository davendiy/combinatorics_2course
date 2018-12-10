#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 10.12.18
# by David Zashkolny
# 2 course, comp math
# Taras Shevchenko National University of Kyiv
# email: davendiy@gmail.com

INF = float('inf')


class Vertex:

    def __init__(self, key):
        self.mKey = key
        self.mData = None
        self.mNeighbors = {}
        self.mVisited = None
        self.mDistance = INF
        self.mSource = None

    def source(self):
        return self.mSource

    def key(self):
        return self.mKey

    def distance(self):
        return self.mDistance

    def neighbors(self):
        return self.mNeighbors

    def set_distance(self, new):
        self.mDistance = new

    def add_neighbor(self, vertex, weight=1):
        self.mNeighbors[vertex] = weight

    def set_source(self, source):
        self.mSource = source

    def set_data(self, data):
        self.mData = data

    def visited(self):
        return self.mDistance != INF

    def set_unvisited(self):
        self.mDistance = INF

    def weight(self, neighbor):
        return self.mNeighbors[neighbor]

    def __str__(self):
        """ Зображення вершини у вигляді рядка у разом з усіма її сусідами """
        return str(self.mKey) + ": Data = " + str(self.mData) + "  Dist = " + str(self.mDistance) + "  From: " + str(
            self.mSource) + ' connected: ' + str(self.mNeighbors)
        # return str(self.mId) + ": Data=" + str(self.getData())

    def __repr__(self):
        """ Зображення вершини у вигляді рядка у разом з усіма її сусідами """
        return str(self.mKey) + ": Data = " + str(self.mData) + "  Dist = " + str(self.mDistance) + "  From: " + str(
            self.mSource) + ' connected: ' + str(self.mNeighbors)
        # return str(self.mId) + ": Data=" + str(self.getData())


class Graph:

    def __init__(self, vertices=None, oriented=False):
        self.mVertexNumber = 0
        self.mVertices = {}
        self.mEdges = []
        self.mIsOriented = oriented
        self.edges = {}
        if vertices is not None:
            for node in vertices:
                self.add_vertex(node)

    def add_vertex(self, vertex):
        if vertex in self:  # Якщо вершина міститься у графі, її вже не треба додавати
            return False

        new_vertex = Vertex(vertex)  # створюємо нову вершину з іменем Vertex
        self.mVertices[vertex] = new_vertex  # додаємо цю вершину до списку вершин графу
        self.mVertexNumber += 1  # Збільшуємо лічильник вершин у графі
        return True

    def add_edge(self, source, destination, weight=1):
        if source not in self:  # Якщо вершина source ще не міститься у графі
            self.add_vertex(source)  # додаємо вершину source
        if destination not in self:  # Якщо вершина destination ще не міститься у графі
            self.add_vertex(destination)  # додаємо вершину destination

        # Встановлюємо зв'язок (тобто ребро) між вершинами source та destination
        self[source].add_neighbor(destination, weight)
        self.edges[(source, destination)] = weight

        if not self.mIsOriented:  # Якщо граф не орієнтований, то треба додати зворотній зв'язок
            self.mVertices[destination].add_neighbor(source, weight)
            self.edges[(destination, source)] = weight

    def set_data(self, vertex, data):
        self[vertex].set_data(data)

    def __contains__(self, vertex) -> Vertex:
        if isinstance(vertex, Vertex):  # Якщо Vertex - вершина (не ім'я)
            return vertex.mKey() in self.mVertices
        else:  # Якщо Vertex - ім'я (ключ) вершини
            return vertex in self.mVertices

    def __iter__(self):
        return iter(self.mVertices.values())

    def __len__(self):
        return self.mVertexNumber

    def __str__(self):
        s = ""
        for vertex in self:
            s = s + str(vertex) + "\n"
        return s

    def __getitem__(self, vertex):
        vertex = vertex.mKey if isinstance(vertex, Vertex) else vertex
        return self.mVertices[vertex]
