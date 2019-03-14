from collections import defaultdict
import sys

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
    while len(visited) != len(g.keys()):
        next = findMin(g, visited)
        visited.add(next[1][0])
        addEdge(path, next[0], next[1])
    return path

def findMin(g, visited):
    min = ("",float("inf"))
    vec = ""
    for v in visited:
        for i in g[v]:
            if i[1] < min[1] and i[0] not in visited:
                min = i
                vec = v
    return (vec, min)

def printPath(path):
    print("graph prim {")
    for v in path:
        for i in path[v]:
            print(v + " -- " + i[0], end='')
            print(" [label=" + str(i[1]) + "];")
    print('}')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = sys.argv[1]
    else:
        f = "city-pairs.txt"
    g = defaultdict(list)
    build(f, g)
    path = mst(g, "Albany")
    printPath(path)
