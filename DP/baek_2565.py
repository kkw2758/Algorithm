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
  cnt = 1
  pre = graph[i]
  for j in range(i + 1, n):
    if pre < graph[j] :
      pre = graph[j]
      cnt += 1
  dp[i] = cnt

print(graph)
print(n - max(dp))
print(dp)