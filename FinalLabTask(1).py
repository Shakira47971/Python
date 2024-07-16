
graph = {
    'A': [('B', 2), ('C', 5), ('D', 4)],
    'B': [('E', 8), ('F', 7)],
    'C': [('G', 9), ('H', 10)],
    'D': [('I', 6)],
    'I': [('J', 3), ('K', 4)],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'J': [],
    'K': []
}

start_node = 'A'
goal_node = 'J'


queue = [(start_node, [start_node], 0)]  

while queue:
    node, path, path_cost = queue.pop(0)

    if node == goal_node:
        print(f"Shortest path from {start_node} to {goal_node}: {path} with total cost {path_cost}")
        break

    for neighbor, edge_cost in graph[node]:
        if neighbor not in path:
            queue.append((neighbor, path + [neighbor], path_cost + edge_cost))
