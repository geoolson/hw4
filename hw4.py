import sys
from collections import defaultdict

def build(f, g):
    f = open(f)
    f = f.readlines()
    for i in f:
        temp = i.split()
        addEdge(g, temp[0], (temp[1], int(temp[2])))

def addEdge(g, vector, edge):
    g[vector].append(edge)

def mst(g, root):
    visited = set()
    path = defaultdict(list)
    visited.add(root)
    next = findMin(g, visited)
    visited.add(next[0])
    addEdge(path, next[0], next[1])


def findMin(g, visited):
    min = ("",float("inf"))
    vec = ""
    for v in visited:
        for i in g[v]:
            if i[1] < min[1] and i is not visited:
                min = i
                vec = v
    return (vec, min)

if __name__ == "__main__":
    g = defaultdict(list)
    f = "city-pairs.txt"
    build(f, g)
    mst(g, "Albany")
