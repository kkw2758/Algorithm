import heapq

INF = int(1e9)
n, m ,a, b, c = list(map(int, input().split()))

distance = [[INF, INF, 0] for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  start, end, cost = map(int, input().split())
  graph[start].append((end, cost))
  graph[end].append((start, cost))

q = []
heapq.heappush(q, (0, a))
distance[a][0] = 0  #통과하는데 드는 금액
distance[a][1] = 0  #이때까지 최고 금액
distance[a][2] = c  #남은돈
while q:
  dist, now = heapq.heappop(q)
  if distance[now][0] < dist:
    continue
  for next_node, next_cost in graph[now]:
    # if dist < distance[next_node][1]: #최소 금액 갱신
    #   distance[next_node][1] = dist
    cost = dist + next_cost
    # print(cost)
    # print(next_node, next_cost)
    # print(cost < distance[next_node][0], cost, distance[next_node][0])
    # print(distance[now][2] >= next_cost)
    # print(dist < distance[next_node][1])
    if cost < distance[next_node][0] and distance[now][2] >= next_cost and next_cost < distance[next_node][1]:
      distance[next_node][2] = distance[now][2] - next_cost #남은 돈
      distance[next_node][0] = cost
      distance[next_node][1] = next_cost
      heapq.heappush(q, (cost, next_node))

for _ in distance:
  print(_)