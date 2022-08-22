# 2022/08/21 Baek 5972
import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue

  for next_node in graph[now]:
    cost = dist + next_node[1]
    if cost < distance[next_node[0]]:
      distance[next_node[0]] = cost
      heapq.heappush(q, (cost, next_node[0]))

print(distance[-1])