# 2023/01/15 Baek 11060

INF = int(1e9)
N = int(input())
maze = list(map(int, input().split()))

dp = [INF] * N
dp[0] = 0

for i in range(len(maze)):
  for j in range(1, maze[i] + 1):
    if i + j > N - 1:
      break
    dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[-1] == INF:
  print(-1)
else:
  print(dp[-1])