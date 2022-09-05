# 2022/09/05 Baek 1389

# 플로이드-워셜
INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for i in range(1, N + 1):
  for j in range(1, N + 1):
    if i == j:
      graph[i][j] = 0

for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

result = INF
min_idx = 0
for i in range(1, N + 1):
  temp = 0
  for j in range(1, N + 1):
    temp += graph[i][j]
  if result > temp:
    result = temp
    min_idx = i

print(min_idx)