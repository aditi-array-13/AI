def heuristic(node):
    # Replace this with your heuristic function to estimate the cost from the current node to the goal
    heuristic_values = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 1,
        'E': 2,
        'G': 0,
    }
    return heuristic_values[node]

def aStarAlgo(start_node, stop_node, graph):
    open_set = set([start_node])
    closed_set = set()
    g = {node: float('inf') for node in graph}
    g[start_node] = 0
    parents = {node: None for node in graph}

    while open_set:
        n = min(open_set, key=lambda node: g[node] + heuristic(node))

        if n == stop_node:
            path = []
            while n is not None:
                path.append(n)
                n = parents[n]
            path.reverse()
            return path

        open_set.remove(n)
        closed_set.add(n)

        for (m, weight) in graph[n]:
            if m in closed_set:
                continue

            tentative_g = g[n] + weight

            if tentative_g < g[m]:
                parents[m] = n
                g[m] = tentative_g
                if m not in open_set:
                    open_set.add(m)

    return None

# Describe your graph here
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)]
}

start_node = 'A'
stop_node = 'G'
path = aStarAlgo(start_node, stop_node, Graph_nodes)
if path:
    print(f'Shortest path from {start_node} to {stop_node}: {path}')
else:
    print('No path exists.')
