'''
import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
matrix = [[] for _ in range(m + 1)]

for _ in range(n):
    like_channel, unlike_channel = map(int, input().split())
    if not matrix[unlike_channel]:
        matrix[unlike_channel].append(like_channel)

visited = [False for _ in range(m + 1)]
def dfs_stack(start_vertex):
    stack = [start_vertex]
    cnt = -1
    while stack:
        vertex = stack.pop()

        if visited[vertex]:
            cnt = -1
            break

        visited[vertex] = True
        cnt += 1
        
        if matrix[vertex]:
            stack.append(matrix[vertex][0])
    
    return cnt

print(dfs_stack(p))
'''


import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
matrix = [0 for _ in range(m + 1)]

for _ in range(n):
    like_channel, unlike_channel = map(int, input().split())
    if not matrix[unlike_channel]:
        matrix[unlike_channel] = like_channel

visited = [False for _ in range(m + 1)]
def dfs_stack(start_vertex):
    stack = [start_vertex]
    cnt = -1
    while stack:
        vertex = stack.pop()

        if visited[vertex]:
            cnt = -1
            break

        visited[vertex] = True
        cnt += 1
        
        if matrix[vertex]:
            stack.append(matrix[vertex])
    
    return cnt

print(dfs_stack(p))