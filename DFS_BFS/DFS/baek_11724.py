'''
def dfs(start_node):
    stack = []
    stack.append(start_node)
    visited[start_node] = True
    #print(start_node, end = ' ')
    while stack:
        node = stack[-1]
        
        cnt = 0
        for m in graph[node]:
            if not(visited[m]):
                visited[m] = True
                stack.append(m)
                #print(m, end = ' ')
                cnt += 1
                break

        if cnt == 0:
            stack.pop()



n, m = map(int,input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for li in graph:
    li.sort()


visited = [0] + [False] * n

result = 0
for x in range(1, n + 1):
    if not(visited[x]):
        dfs(x)
        result += 1

print(result)
'''


'''
import sys
sys.setrecursionlimit(100000)

def recursive_dfs(start_node):
    visited[start_node] = True

    for node in graph[start_node]:
        if not(visited[node]):
            recursive_dfs(node)


n, m = map(int,input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    #graph[v].append(u)


visited = [0] + [False] * n

result = 0
for x in range(1, n + 1):
    if not(visited[x]):
        recursive_dfs(x)
        result += 1

print(result)
'''

import sys
sys.setrecursionlimit(100000)

def recursive_dfs(start_node):
    visited[start_node] = True

    for node in graph[start_node]:
        if not(visited[node]):
            recursive_dfs(node)


n, m = map(int,input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int,input().split())
    graph[v].append(u)
    graph[u].append(v)

visited = [0] + [False] * n

result = 0
for x in range(1, n + 1):
    if not(visited[x]):
        recursive_dfs(x)
        result += 1

print(result)