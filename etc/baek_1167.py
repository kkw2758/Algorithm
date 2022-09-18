# 2022/09/17 Baek 1167

import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def dfs(start):
  distance = [INF] * (V + 1)
  q = deque()
  q.append((start, 0))
  distance[start] = 0

  while q:
    now, cost = q.popleft()
    for next_node, next_cost in graph[now]:
      if cost + next_cost < distance[next_node]:
        distance[next_node] = cost + next_cost
        q.append((next_node, cost + next_cost))
  return distance


def find_max_idx(ary):
  max_idx = 1
  for i in range(2, len(ary)):
    if ary[max_idx] < ary[i]:
      max_idx = i

  ary[max_idx] = 0
  return max_idx


V = int(input())
graph = [set() for _ in range(V + 1)]
for _ in range(V):
  info = list(map(int, input().rstrip().split()))[:-1]
  start = info[0]
  info = info[1:]
  for i in range(len(info) // 2):
    end, cost = info[i * 2: (i + 1) * 2]
    graph[start].add((end, cost))
    graph[end].add((start, cost))

result = dfs(1)
start_point = find_max_idx(result)

print(max(dfs(start_point)[1:]))