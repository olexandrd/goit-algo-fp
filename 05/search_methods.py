from collections import deque


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)
    result = [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    result = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return result

def dfs_recursive_steps(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    
    for neighbor in graph[vertex]:
        print(f"|Node: {vertex}| neighbor: {neighbor}| Visited: {visited}|")
        if neighbor not in visited:
            dfs_recursive_steps(graph, neighbor, visited)


def bfs_recursive_steps(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(f"|Node: {vertex}| Queue: {queue}| Visited: {visited}|")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive_steps(graph, queue, visited)

if __name__ == "__main__":
    print("Do not run this file")
