# import heapq
# import sys


# INF = int(1e9)

# input = sys.stdin.readline
# n, m, c = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)


# for _ in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y, z))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0

#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]

#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(c)

# max_time = 0
# city_count = 0
# for time in distance:
    
#     if time == INF or time == 0:
#         continue

#     city_count += 1

#     if max_time < time:
#         max_time = time

# print(city_count, max_time)


import sys
import heapq

INF = int(1e9)


n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
    
def get_smallest_node():
    min_value = INF
    min_idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            min_idx = i
    return min_idx

def dijkstra(start):
    visited[start] = False
    distance[start] = 0
    
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(c)
result = [0,0]
for i in range(1, n + 1):
    if distance[i] < INF and distance[i] > 0:
        result[0] += 1
        result[1] = max(result[1], distance[i])

print(result[0], result[1])

import sys
import heapq

INF = int(1e9)


n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(distance[i[0]],i[0]))

dijkstra(c)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count -1, max_distance)