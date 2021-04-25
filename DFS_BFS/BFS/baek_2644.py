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



'''
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
'''