import heapq

class Node:
    def __init__(self, name, g=0, h=0, parent=None):
        self.name = name
        self.g = g  
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(graph, heuristic, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start, g=0, h=heuristic[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.name == goal:
            path = []
            total_cost = current_node.g
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1], total_cost  # Return reversed path and total cost

        closed_list.add(current_node.name)

        for neighbor, cost in graph[current_node.name]:
            if neighbor in closed_list:
                continue

            g = current_node.g + cost
            h = heuristic[neighbor]
            f = g + h

            neighbor_node = Node(neighbor, g, h, parent=current_node)
            heapq.heappush(open_list, neighbor_node)

    return None, float('inf')

graph = {
    'S': [('A', 3), ('B', 3), ('C', 5)],
    'A': [('D', 7), ('E', 10)],
    'B': [('C', 5)],
    'C': [('E', 2), ('F', 6)],
    'D': [('G', 6)],
    'E': [('G', 3)],
    'F': [('G', 6)],
    'G': []  
}

heuristic = {
    'S': 40, 'A': 35, 'B': 32, 'C': 25, 'D': 30, 'E': 15, 'F': 20, 'G': 0
}

start = 'S'
goal = 'G'
path, total_cost = a_star_search(graph, heuristic, start, goal)

if path:
    print(f"Optimal path: {' -> '.join(path)}")
    print(f"Total cost: {total_cost}")
else:
    print("Goal is not reachable")
