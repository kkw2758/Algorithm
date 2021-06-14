import sys

n, m, v = map(int, sys.stdin.readline().strip().split())
visited = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().strip().split())
    graph[start].append(end)
    graph[end].append(start)


for idx in range(1, n + 1):
    graph[idx].sort(reverse=True)


'''
def dfs(start_vertex):
    visited[start_vertex] = 1
    print(start_vertex, end = " ")

    for i in graph[start_vertex]:
        if not visited[i]:
            dfs(i)

dfs(v)
'''
def dfs_st(start_vertex):
    stack = [start_vertex]

    while stack:
        now_vertex = stack.pop()
        
        
        if not visited[now_vertex]:
            visited[now_vertex] = 1
            print(now_vertex, end = " ")
            #stack.extend(graph[now_vertex])
            stack += graph[now_vertex]

dfs_st(v)
print("")


from collections import deque

def bfs(start_vertex):
    queue = deque([start_vertex])
    visited[start_vertex] = 1

    while queue:
        now_vertex = queue.popleft()
        print(now_vertex, end = " ")

        for next_vertex in graph[now_vertex][::-1]:
            if not visited[next_vertex]:
                queue.append(next_vertex)
                visited[next_vertex] = 1

visited = [0 for _ in range(n + 1)]
bfs(v)




'''
def dfs_stack(start_vertex):
    stack = [start_vertex]

    while stack:
        
        now_vertex = stack[-1]
        if not visited[now_vertex]:
            visited[now_vertex] = 1
            print(now_vertex, end = ' ')

        cnt = 0

        for next_vertex in graph[now_vertex]:
            if not visited[next_vertex]:
                stack.append(next_vertex)
                cnt = 1
                break

        if not cnt:
            stack.pop()
dfs_stack(v)
print("")
'''
