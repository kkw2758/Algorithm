import heapq

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)  
    if dist > distance[now]:
      continue

    for next_node in graph[now]:
      cost = dist + next_node[1]    
      if cost < distance[next_node[0]]:
        distance[next_node[0]] = cost
        heapq.heappush(q, (cost, next_node[0]))

dijkstra(1)
max_value = max(distance[1:])
min_house = distance.index(max_value)
count = distance.count(max_value)

print(min_house, max_value, count)
