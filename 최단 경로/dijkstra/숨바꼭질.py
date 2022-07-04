import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

distance = [INF] * (n + 1)

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
        heapq.heappush(q, (cost, i[0]))

dijkstra(1)

max_value = 0
for i in range(n):
  if distance[i] < INF:
    if max_value < distance[i]:
      max_value = distance[i]

cnt = distance.count(max_value)
first_max_value_idx = distance.index(max_value)

print(first_max_value_idx, max_value, cnt)