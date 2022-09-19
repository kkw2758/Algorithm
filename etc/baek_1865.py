# 2022/09/19 Baek 1865

# import heapq
# import sys

# INF = int(1e9)
# input = sys.stdin.readline

# def dijkstra(start):
#   distance = [INF] * (N + 1)
#   q = []
#   heapq.heappush(q, (0, start))
#   distance[start] = 0
  
#   while q:
#     cost, now = heapq.heappop(q)
#     if distance[start] < 0:
#       break
#     if distance[now] < cost:
#       continue
#     for next_node, next_cost in graph[now]:
#       new_cost = cost + next_cost
#       if new_cost < distance[next_node]:
#         distance[next_node] = new_cost
#         heapq.heappush(q, (new_cost, next_node))
#   print("dijkstra{}".format(start),distance)
#   return distance


# TC = int(input())
# for _ in range(TC):
#   N, M, W = map(int, input().split())
#   graph = [[] for _ in range(N + 1)]

#   for _ in range(M):
#     S, E, T = map(int, input().split())
#     graph[S].append((E, T))
#     graph[E].append((S, T))

#   for _ in range(W):
#     S, E, T = map(int, input().split())
#     graph[S].append((E, -T))

#   result = "NO"
#   for i in range(1, N + 1):
#     if dijkstra(i)[i] < 0:
#       result = "YES"
#       break

#   print(result)

import sys

input = sys.stdin.readline
INF = int(1e9)

# def bf(start):
#   dis = [INF] * (n + 1)
#   dis[start] = 0

#   for i in range(n):
#     for edge in edges:
#       cur = edge[0]
#       next_node = edge[1]
#       cost = edge[2]

#       if dis[cur] != INF and dis[next_node] > cost + dis[cur]:
#         dis[next_node] = cost + dis[cur]

#         if i == n - 1:
#           return True

#   return False

import sys
input = sys.stdin.readline
INF = int(1e9)

# 벨만 포드 알고리즘
def bf(start):
    dist = [INF] * (n + 1)
    # dist[start] = 0
    for i in range(n): # 정점 수만큼 반복
        for j in range(len(edges)): # 매 반복 마다 모든 간선 확인
            node = edges[j][0] # 현재 노드 받아오기
            next_node = edges[j][1] # 다음 노드 받아오기
            cost = edges[j][2] # 가중치 받아오기
            # 현재 간선을 거려서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1: # n-1번 이후 반복에도 값이 갱신되면 음수 순환 존재
                    return True
    return False

t = int(input())

for _ in range(t):
  n, m, w = map(int, input().split())
  edges = []
  for _ in range(m):
    s, e, t = map(int, input().split())
    edges.append((s, e, t))
    edges.append((e, s, t))

  for _ in range(w):
    s, e, t = map(int, input().split())
    edges.append((s, e, -t))

  key = bf(1)

  if key:
    print("YES")
  else:
    print("NO")