# 2022/09/27 Baek 2565

n = int(input())
graph = []
dp = [1] * n

for _ in range(n):
  a, b = map(int, input().split())
  graph.append((a, b))

graph.sort()
graph = [member[1] for member in graph]

for i in range(n):
  for j in range(i):
    if graph[i] > graph[j] :
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))


