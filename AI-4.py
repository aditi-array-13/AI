'''Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking
for a graph coloring problem.'''

def is_safe(graph, v, c, color, n, result):
    for i in range(n):
        if graph[v][i] and color[i] == c:
            return False
    return True

def graph_coloring_bb_util(graph, m, color, v, n, result):
    if v == n:
        result.append(color[:])
        return

    for c in range(1, m + 1):
        if is_safe(graph, v, c, color, n, result):
            color[v] = c
            graph_coloring_bb_util(graph, m, color, v + 1, n, result)
            color[v] = 0

def graph_coloring_bb(graph, m):
    n = len(graph)
    result = []
    color = [0] * n
    graph_coloring_bb_util(graph, m, color, 0, n, result)
    return result

def graph_coloring_backtracking(graph, m):
    n = len(graph)
    result = [-1] * n

    def is_valid(v, c):
        for i in range(n):
            if graph[v][i] and result[i] == c:
                return False
        return True

    def graph_coloring_util(v):
        if v == n:
            return True

        for c in range(1, m + 1):
            if is_valid(v, c):
                result[v] = c
                if graph_coloring_util(v + 1):
                    return True
                result[v] = -1

    if not graph_coloring_util(0):
        return []

    return result

# Example usage:
graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]
m = 3  # Number of colors

print("Graph Coloring using Branching and Bound:")
bb_result = graph_coloring_bb(graph, m)
if bb_result:
    for idx, coloring in enumerate(bb_result):
        print(f"Solution {idx + 1}: {coloring}")

print("\nGraph Coloring using Backtracking:")
backtrack_result = graph_coloring_backtracking(graph, m)
if backtrack_result:
    print("Solution:", backtrack_result)
else:
    print("No valid coloring found.")
