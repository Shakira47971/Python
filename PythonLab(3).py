def input_graph():
    graph = {}
    print("Enter node and its neighbors (type 'done' when finished):")
    while True:
        line = input().strip()
        if line.lower() == 'done':
            break
        parts = line.split()
        node = parts[0]
        neighbors = parts[1:]
        graph[node] = neighbors

        for neighbor in neighbors:
            if neighbor not in graph:
                graph[neighbor] = []
    return graph

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def dfs_full(graph, start_node):
    visited = set()
    dfs(graph, start_node, visited)

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)

if __name__ == "__main__":
    graph = input_graph()
    start_node = input("Enter the start node: ").strip()
    print(f"\nFollowing is the Depth-First Search of the entire graph starting from node {start_node}:")
    dfs_full(graph, start_node)
