#2022/10/11 baek_14889

# brute-force
from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
number = []
result = int(1e9)
for i in range(n):
    number.append(list(map(int, input().split())))

start_candidates = list(combinations([i for i in range(1, n + 1)], n // 2))

for start_candidate in start_candidates:
    link_candidate = tuple(set([i for i in range(1, n + 1)]) - set(start_candidate))
    start_score = 0
    link_score = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            start_score += number[start_candidate[i] - 1][start_candidate[j] - 1]
            start_score += number[start_candidate[j] - 1][start_candidate[i] - 1]
            link_score += number[link_candidate[i] - 1][link_candidate[j] - 1]
            link_score += number[link_candidate[j] - 1][link_candidate[i] - 1]
            
    result = min(result, abs(start_score - link_score))
    
print(result)

# Backtracking
def dfs(depth, idx):
  global min_dif
  if depth == n // 2:
    power1, power2 = 0, 0
    for i in range(n):
      for j in range(n):
        if visited[i] and visited[j]:
          power1 += graph[i][j]
        elif not visited[i] and not visited[j]:
          power2 += graph[i][j]

    min_dif = min(min_dif, abs(power1 - power2))
    return
  else:
    for i in range(idx, n):
      if visited[i] == False:
        visited[i] = True
        dfs(depth + 1, i + 1)
        visited[i] = False

n = int(input())
visited = [False] * n
graph = [list(map(int, input().split())) for _ in range(n)]
min_dif = int(1e9)

dfs(0,0)
print(min_dif)