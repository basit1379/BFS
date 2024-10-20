# Islamabad is connected to Rawalpindi, Lahore, and Peshawar. 
# Rawalpindi is connected to Islamabad, Peshawar, and Quetta. 
# Peshawar is connected to Islamabad, Rawalpindi, and Quetta. 
# Lahore is connected to Islamabad, Multan, and Quetta. 
# Multan is connected to Lahore, Karachi, and Quetta. 
# Quetta is connected to Rawalpindi, Peshawar, Multan, and Karachi. 
# Karachi is connected to Multan and Quetta.

from collections import deque
def bfs(graph, start_node, goal_node):
    queue = deque([[start_node]])
    visited = set([start_node])

    while queue:
        path = queue.popleft()
        current_node = path[-1]

        if current_node == goal_node:
            return path
        

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path) + [neighbor] 
                queue.append(new_path)

    return None

pakistan_graph = {
    'Islamabad': ['Rawalpindi', 'Lahore', 'Peshawar'],
    'Rawalpindi': ['Islamabad', 'Peshawar', 'Quetta'],
    'Peshawar': ['Islamabad', 'Rawalpindi', 'Quetta'],
    'Lahore': ['Islamabad', 'Multan', 'Quetta'],
    'Multan': ['Lahore', 'Karachi', 'Quetta'],
    'Quetta': [ 'Rawalpindi', 'Peshawar', 'Multan', 'Karachi'],
    'Karachi': ['Multan', 'Quetta']
}
shortest_path = bfs(pakistan_graph, 'Islamabad', 'Karachi')

print("Shortest path from Islamabad to Karachi: ", shortest_path)