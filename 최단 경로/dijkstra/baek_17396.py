# 2022/08/21 Baek 17396

# import heapq
# import sys

# INF = int(1e9)
# input = sys.stdin.readline
# n, m = map(int, input().split())
# distance = [INF for _ in range(n)]
# can = list(map(int, input().split()))
# can[-1] = 0

# graph = [[] for _ in range(n)]

# for _ in range(m):
#   a, b, c = map(int, input().split())
#   graph[a].append((b,c))
#   graph[b].append((a,c))

# q = []
# heapq.heappush(q, (0, 0))
# distance[0] = 0

# while q:
#   dist, now = heapq.heappop(q)
#   if distance[now] < dist:
#     continue 
  
#   for next_node, next_dist in graph[now]:
#     cost = dist + next_dist
#     if cost < distance[next_node] and can[next_node] == 0:
#       distance[next_node] = cost
#       heapq.heappush(q, (cost, next_node))

# result = distance[-1]
# if distance[-1] == INF:
#   print(-1)
# else:
#   print(result)


# 2022/08/21 Baek 17396

import heapq
import sys

input = sys.stdin.readline
INF = int(10e9)

n, m = map(int, input().split())
sight_information = list(map(int, input().split()))
distance = [INF] * (n)
graph = [[] for _ in range(n)]

for _ in range(m):
  a, b, c = map(int, input().split())
  if (a != n - 1 and sight_information[a] == 1) or (b != n - 1 and sight_information[b] == 1):
    continue
  graph[a].append((b, c))
  graph[b].append((a, c))

q = []
heapq.heappush(q, (0, 0))
distance[0] = 0

while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for next_node in graph[now]:
    cost = dist + next_node[1]
    if cost < distance[next_node[0]]:
      distance[next_node[0]] = cost
      heapq.heappush(q, (cost, next_node[0]))

if distance[-1] == INF:
  print(-1)
else:
  print(distance[-1])