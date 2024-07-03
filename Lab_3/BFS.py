from collections import deque

def bfs(graph, start):
    visited = set()      #Множество для отслеживания посещённых вершин
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()   #Извлечение вершины из начала очереди
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)  #Добавление вершины в список результатов обхода
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited) #Добавление в очередь всех соседей текущей вершины, которые ещё не были посещены
    
    return result

#Primer vershin 
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': ['H', 'I'],
        'F': [],
        'G': [],
        'H': [],
        'I': []
    }
    
    start_node = 'A'
    bfs_result = bfs(graph, start_node)
    print("BFS traversal starting from node {}: {}".format(start_node, bfs_result))
