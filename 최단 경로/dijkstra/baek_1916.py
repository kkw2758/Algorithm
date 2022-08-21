import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for next_node in graph[now]:
    cost = dist + next_node[1]
    if cost < distance[next_node[0]]:
      distance[next_node[0]] = cost
      heapq.heappush(q, (cost, next_node[0]))

print(distance[end])