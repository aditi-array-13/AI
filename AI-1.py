#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''1. Implement depth first search algorithm and Breadth First Search algorithm. Use an undirected graph and
develop a recursive algorithm for searching all the vertices of a graph or tree data structure.'''
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, v):
        visited = [False] * (max(self.graph) + 1)
        self.dfs_recursive(v, visited)

    def bfs(self, v):
        visited = [False] * (max(self.graph) + 1)
        queue = []

        visited[v] = True
        queue.append(v)

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

# Create a sample graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Search (DFS) starting from vertex 2:")
g.dfs(3)

print("\nBreadth-First Search (BFS) starting from vertex 3:")
g.bfs(3)


# In[ ]:




