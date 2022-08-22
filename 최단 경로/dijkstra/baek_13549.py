# 2022/08/21 Baek 13549
# import heapq

# n, k = map(int, input().split())

# INF = int(1e9)
# graph = [[] for _ in range(100001)]
# distance = [INF for _ in range(100001)]

# for i in range(100001):
#   graph[i].append((i - 1, 1))
#   if i + 1 > 100000:
#     continue
#   graph[i].append((i + 1, 1))
#   if i * 2 > 100000:
#     continue
#   graph[i].append((i * 2, 0))

# q = []
# heapq.heappush(q, (0, n))
# distance[n] = 0

# while q:
#   dist, now = heapq.heappop(q)
#   if distance[now] < dist:
#     continue
#   for next_node in graph[now]:
#     cost = dist + next_node[1]
#     if cost < distance[next_node[0]]:
#       distance[next_node[0]] = cost
#       heapq.heappush(q, (cost, next_node[0]))

# print(distance[k])


from collections import deque

n, k = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(100001)]
distance = [INF for _ in range(100001)]

for i in range(100001):
  graph[i].append((i - 1, 1))
  if i + 1 > 100000:
    continue
  graph[i].append((i + 1, 1))
  if i * 2 > 100000:
    continue
  graph[i].append((i * 2, 0))

q = []
queue = deque([n])
distance[n] = 0
while queue:
  now = queue.popleft()
  for next_node, dist in graph[now]:
    if distance[now] + dist < distance[next_node]:
      distance[next_node] = distance[now] + dist
      queue.append(next_node)

print(distance[k])