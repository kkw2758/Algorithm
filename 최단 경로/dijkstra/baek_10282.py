# 2022/08/25 Baek 10282

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n, d, c = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  total_time_list = [INF] * (n + 1)
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b].append((a, s))

  result = 0
  q = []
  heapq.heappush(q, (0, c))  #소요 시간, 현재 노드
  total_time_list[c] = 0

  while q:
    time, now  = heapq.heappop(q)
    if total_time_list[now] < time:
      continue
    for next_node, next_time in graph[now]:
      total_time = time + next_time
      if total_time < total_time_list[next_node]:
        total_time_list[next_node] = total_time
        heapq.heappush(q, (total_time, next_node))

  cnt = 0
  result = 0
  for total_time in total_time_list:
    if total_time != INF:
      result = max(result, total_time)
      cnt += 1

  print(cnt, result)