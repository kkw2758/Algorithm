import sys

INF = 1e9
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

x, k = map(int, input().split())

def get_smallest_node():
    min_value = INF
    min_idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            min_idx = i
    
    return min_idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

visited = [False] * (n + 1)
distance = [INF] * (n + 1)

dijkstra(1)
result1 = distance[k]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)
dijkstra(k)
result2 = distance[x]

result = result1 + result2

if result >= INF:
    print(-1)
else:
    print(result)


'''
ex1)
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

ex2)
4 2
1 3
2 4
3 4
'''


import sys
import heapq

INF = 1e9
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

x, k = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, i[0]))

distance = [INF] * (n + 1)

dijkstra(1)
result1 = distance[k]
distance = [INF] * (n + 1)
dijkstra(k)
result2 = distance[x]

result = result1 + result2

if result >= INF:
    print(-1)
else:
    print(result)