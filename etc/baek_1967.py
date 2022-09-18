# 2022/09/17 Baek 1967

from collections import deque
import sys
input = sys.stdin.readline


def dfs(start):
  distance = [INF] * (N + 1)
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

INF = int(1e9)
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))


result = dfs(1)
first = find_max_idx(result)

result = dfs(first)
print(max(result[1:]))