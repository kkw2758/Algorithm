# 2022/08/21 Baek 1446

# N, D = map(int, input().split())
# informations = []
# dp = [x for x in range(D + 1)]

# for _ in range(N):
#   informations.append(list(map(int, input().split())))

# informations.sort()

# for information in informations:
#   start, end, cost = information
#   if end > D:
#     continue
#   distance = dp[end] - dp[start]
#   if distance > cost:
#     cnt = 0
#     for i in range(end, D + 1):
#       # dp[end] = dp[start] + cost
#       if dp[i] < dp[start] + cost + cnt:
#         break
#       dp[i] = dp[start] + cost + cnt
#       cnt += 1

# print(dp[-1])

import heapq

INF = int(1e9)
n, d = map(int, input().split())
distance = [INF] * (d + 1)
graph = [[] for _ in range(d + 1)]

for i in range(d):
  graph[i].append((i + 1, 1))

for _ in range(n):
  a, b, c = list(map(int, input().split()))
  if b > d:
    continue
  graph[a].append((b, c))

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

print(distance[-1])
