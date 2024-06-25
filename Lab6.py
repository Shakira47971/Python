def iterative_deepening_dfs(graph, start, goal, max_depth):
    for depth in range(3, max_depth + 1):  
        path = dfs_limited(graph, start, goal, depth)
        if path:
            return path
    return None

def dfs_limited(graph, node, goal, depth, path=None):
    if path is None:
        path = []

    path.append(node)

    if node == goal:
        return path

    if depth <= 0:
        path.pop()
        return None

    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = dfs_limited(graph, neighbor, goal, depth - 1, path)
            if result:
                return result

    path.pop()
    return None


graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

start = 0
goal = 5
max_depth = 3

path = iterative_deepening_dfs(graph, start, goal, max_depth)

if path:
    print("Path found:", path)
else:
    print("No path found within the specified depth.")
