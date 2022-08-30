# 2022/08/30 Baek 1277

import sys, heapq
import math

input = sys.stdin.readline

INF = int(1e9)
N, W = map(int, input().split())
M = float(input())
distance = [INF] * (N + 1)
house = [[]]
for _ in range(N):
  house.append(list(map(int, input().rstrip().split())))

load = set()
for _ in range(W):
  a, b = map(int, input().split())
  load.add((a, b))
  load.add((b, a))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    now_x, now_y = house[now]

    for next_node in range(1, N + 1):
      if next_node == now:
        continue

      if (now, next_node) in load:
        if distance[now] < distance[next_node]:
          distance[next_node] = distance[now]
          heapq.heappush(q, (distance[next_node], next_node))
        continue

      next_x, next_y = house[next_node]
      next_dist = math.sqrt((now_x - next_x) ** 2 + (now_y - next_y) ** 2)
      total_dist = next_dist + dist
      if next_dist <= M and total_dist < distance[next_node]:
        distance[next_node] = total_dist
        heapq.heappush(q, (total_dist, next_node))

  return distance

result = int(dijkstra(1)[-1] * 1000)
print(result)