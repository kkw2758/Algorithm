#DFS

def dfs(graph, start_node, visited):
    visited[start_node] = True
    print(start_node, end=" ")
    
    for i in graph[start_node]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
dfs(graph, 1, visited)
print("\n")

from collections import deque

def bfs(graph, start_node, visited):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        print(node, end = " ")
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
bfs(graph, 1, visited)