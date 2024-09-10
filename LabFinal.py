# Define the graph as a dictionary of nodes and their neighbors
graph = {
    'S': {'A': 10, 'B': 5, 'C': 7},
    'A': {'D': 2},
    'B': {'E': 4, 'F': 6},
    'C': {'G': 3},
    'D': {},
    'E': {},
    'F': {},
    'G': {}
}
 
# Define the heuristic function (h)
heuristic = {
    'S': 13,
    'A': 8,
    'B': 6,
    'C': 5,
    'D': 0,
    'E': 0,
    'F': 3,
    'G': 0
}
 
# Define the start and goal nodes
start_node = 'S'
goal_nodes = ['D', 'E', 'G']
 
# Define a function to calculate the total cost of a path
def path_cost(path):
  cost = 0
  for i in range(len(path) - 1):
    cost += graph[path[i]][path[i+1]]
  return cost
 
# Define the A* search algorithm
def a_star_search(start_node, goal_nodes):
 
  g_score = {node: float('inf') for node in graph}
  g_score[start_node] = 0
 
  # Create a dictionary to store the parent node of each node in the path
  parent = {node: None for node in graph}
 

  open_list = [start_node]
 
 
  closed_list = []
 
  # While there are still nodes to explore
  while open_list:
    
    current_node = min(open_list, key=lambda node: g_score[node] + heuristic[node])
 
    # If the current node is a goal node
    if current_node in goal_nodes:
      # Reconstruct the path from the start node to the current node
      path = [current_node]
      while parent[current_node]:
        current_node = parent[current_node]
        path.insert(0, current_node)
      return path
 
   
    open_list.remove(current_node)
 
    
    closed_list.append(current_node)
 
   
    for neighbor in graph[current_node]:
      # If the neighbor is not in the closed list
      if neighbor not in closed_list:
      
        n_g_score = g_score[current_node] + graph[current_node][neighbor]
 
        
        if n_g_score < g_score[neighbor]:
          # Update the g-score and parent for the neighbor
          g_score[neighbor] = n_g_score
          parent[neighbor] = current_node
 
          # Add the neighbor to the open list if it is not already in it
          if neighbor not in open_list:
            open_list.append(neighbor)
 
  
  return None
 
# Find the shortest path to each goal node
for goal_node in goal_nodes:
  path = a_star_search(start_node, [goal_node])
  if path:
    print(f'Path to {goal_node}: {path}')
    print(f'Cost to {goal_node}: {path_cost(path)}')
  else:
    print(f'No path found to {goal_node}')
 
# Find the nearest  node
nearest_node = min(goal_nodes, key=lambda node: path_cost(a_star_search(start_node, [node])))
print(f'Nearest treasure node: {nearest_node}')
