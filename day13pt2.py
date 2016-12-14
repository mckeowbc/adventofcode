#!/usr/bin/env python

import sys
from collections import defaultdict,deque

inf = float('inf')

def isEven(n):
    c = 0
    while n:
        if n & 0x1 == 1:
            c += 1
        n >>= 1
    return c % 2 == 0
    
def isOdd(n):
    return not isEven(n)
    
def buildGrid(x,y,f):
    grid = [
        ['.' for i in range(x) ]
            for j in range(y)
    ]
    
    for r in range(y):
        for c in range(x):
            n = (c**2 + 3*c + 2*r*c + r + r**2) + f
            
            if isOdd(n):
                grid[r][c] = '#'
    return grid
    
def getEdges(node,grid):
    neighbors = filter(lambda x:grid[x[1]][x[0]] == '.',
        filter(lambda x: x[0] >= 0 and x[1] >= 0 \
                            and x[1] < len(grid) and x[0] < len(grid[x[1]]),
                [(node[0],node[1]+r) for r in (-1,1)] + \
                [(node[0]+c,node[1]) for c in (-1,1)])
    )
                    
    return neighbors


class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = set()
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)
    self.edges.add((value,value))
    self.distances[(value,value)] = 0

  def add_edge(self, from_node, to_node, distance):
    self.edges.add((from_node,to_node))
    self.edges.add((to_node, from_node))
    self.distances[(from_node,to_node)]  = distance
    self.distances[(to_node, from_node)] = distance

  def dijkstra(self, source, dest):
        assert source in self.nodes
        dist = {vertex: inf for vertex in self.nodes}
        previous = {vertex: None for vertex in self.nodes}
        dist[source] = 0
        q = self.nodes.copy()
        neighbours = {vertex: set() for vertex in self.nodes}
        for edge in self.edges:
            neighbours[edge[0]].add((edge[1], self.distances[edge]))
        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

def printGrid(grid):
    for r in grid:
        print ' '.join(r)
    print ''

if __name__ == '__main__':
    n = int(sys.argv[1])
    f = int(sys.argv[2])
    
    grid = buildGrid(n+1,n+1,f)

    printGrid(grid)

    g = Graph()

    for y,r in enumerate(grid):
        for x,c in enumerate(r):
            if c == '.':
                g.add_node((x,y))
            
    for node in g.nodes:
        edges = getEdges(node,grid)
        for e in edges:
            g.add_edge(node,e,1)
    
    count = 0 
    for i,node in enumerate(sorted(g.nodes)):
        md = node[0] - 1 + node[1] -1
        
        if md > n:
            continue
        path = g.dijkstra((1,1), node)
        
        if path[0] == (1,1) and path[-1] == node and len(path)-1 <= n:
            print i,count,node,len(path)
            count += 1
    print count