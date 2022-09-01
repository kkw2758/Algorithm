# # 2022/09/01 Baek 14221

# import sys, heapq

# INF = sys.maxsize
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for i in range(m):
#   a, b, c = map(int, input().split())
#   graph[a].append((b, c))
#   graph[b].append((a, c))

# p, q = map(int, input().split())
# house_candidates = list(map(int, input().rstrip().split()))
# house_candidates.sort()
# convenience_store_list = list(map(int, input().rstrip().split()))

# def dijkstra(start):
#   temp = []
#   distance = [INF] * (n + 1)
#   q = []
#   heapq.heappush(q, (0, start))
#   distance[start] = 0
#   while q:
#     dist, now = heapq.heappop(q)
#     if now in convenience_store_list:
#       return dist
#     for next_node, next_dist in graph[now]:
#       cost = dist + next_dist
#       if cost < distance[next_node]:
#         distance[next_node] = cost
#         heapq.heappush(q, (cost, next_node))


# result = []
# for house_candidate in house_candidates:
#   dist = dijkstra(house_candidate)
#   result.append((dist, house_candidate))

# result.sort()
# print(result[0][1])


# 2022/09/01 Baek 14221

import sys, heapq

INF = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

p, q = map(int, input().split())
house_candidates = list(map(int, input().rstrip().split()))
convenience_store_list = list(map(int, input().rstrip().split()))
distance = [INF] * (n + 1)

for convenience_store in convenience_store_list:
  q = []
  heapq.heappush(q, (0, convenience_store))
  distance[convenience_store] = 0
  while q:
    dist, now = heapq.heappop(q)
    if now in house_candidates:
      break
    for next_node, next_dist in graph[now]:
      cost = dist + next_dist
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

result = []
for house_candidate in house_candidates:
  result.append((distance[house_candidate], house_candidate))
result.sort()
print(result[0][1])