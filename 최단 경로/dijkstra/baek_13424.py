# 2022/08/25 Baek 13424

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  distance = [INF] * (n + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next_node, next_cost in graph[now]:
      cost = dist + next_cost
      if distance[next_node] > cost:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

  return distance

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  graph = [[] for _ in range(n + 1)]

  for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

  k = int(input())
  friends = list(map(int, input().split()))

  friends_distance = []
  for friend in friends:
    friends_distance.append(dijkstra(friend))

  distance = [INF] 
  for i in range(1, n + 1):
    temp = 0
    for friend_distance in friends_distance:
      temp +=friend_distance[i]
    distance.append(temp)
    
  min_idx = 0
  for i in range(len(distance)):
    if distance[min_idx] > distance[i]:
      min_idx = i

  print(min_idx)