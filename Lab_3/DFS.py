def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

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
    dfs_result = dfs(graph, start_node)
    print("DFS traversal starting from node {}: {}".format(start_node, dfs_result))
