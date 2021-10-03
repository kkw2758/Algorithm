import sys
from collections import deque

n = int(sys.stdin.readline().strip())
a, b = map(int, sys.stdin.readline().strip().split())

m = int(sys.stdin.readline().strip())
graph = {}

for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    
    if x not in graph.keys():
        graph[x] = [y]
    else:
        graph[x].append(y)

    if y not in graph.keys():
        graph[y] = [x]
    else:
        graph[y].append(x)

visited = [0 for _ in range(n + 1)]

#level이라는 변수를 사용하지 않고 visited배열이 방문여부와 깊이까지 같이 가지도록
def bfs(start_vertex):
    queue = deque([start_vertex])
    while queue:
        now_vertex = queue.popleft()
        for next_vertex in graph[now_vertex]:
            if not visited[next_vertex]:
                queue.append(next_vertex)
                visited[next_vertex] = visited[now_vertex] + 1
bfs(a)
if visited[b]:
    print(visited[b])
else:
    print(-1)




#처음 생각한 풀이
def bfs(start_vertex, target_vertex):
    queue = deque([start_vertex])
    visited[start_vertex] = 1
    level = 0
    
    while queue:
        n = len(queue)
        #print("-----level{}-----".format(level))
        for _ in range(n):
            now_vertex = queue.popleft()
            #print(now_vertex, end = " ")
            if now_vertex == target_vertex:
                return level

            for next_vertex in graph[now_vertex]:
                if not visited[next_vertex]:
                    queue.append(next_vertex)
                    visited[next_vertex] = 1

        level += 1

    return -1

print(bfs(a,b))



import sys
from collections import deque

n = int(sys.stdin.readline().strip())
a, b = map(int, sys.stdin.readline().strip().split())

m = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)

dist = [0 for _ in range(n + 1)]


def bfs(start_vertex, target_vertex):
    queue = deque([start_vertex])
    
    while queue:
        now_vertex = queue.popleft()
        if now_vertex == target_vertex:
            return dist[now_vertex]
        for i in graph[now_vertex]:
            if dist[i] == 0:
                queue.append(i)
                dist[i] = dist[now_vertex] + 1
    
    return -1

print(bfs(a, b))




# 복습
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
x, y = map(int, input().strip().split())
m = int(input())
graph = {}
visited = [False for _ in range(n+1)]

for i in range(m):
    parent, child = map(int, input().strip().split())
    if parent in graph:
        graph[parent].append(child)
    else:
        graph[parent] = [child]
    
    if child in graph:
        graph[child].append(parent)
    else:
        graph[child] = [parent]

def bfs(start, target):
    queue = deque()
    queue.append((start, 0))

    while queue:
        node = queue.popleft()
        visited[node[0]] = True

        if node[0] == target:
            return node[1]

        for member in graph[node[0]]:
            if not(visited[member]):
                queue.append((member, node[1] + 1))
        

    return -1

print(bfs(x, y))