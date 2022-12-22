# 2022/12/22 Baek 14430

# 백트래킹 시간초과
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# dx = [0, 1]
# dy = [1, 0]

# result = []
# def dfs(x, y, cnt):
#   if (x, y) == (N - 1, M - 1):
#     result.append(cnt)
#     return
  
#   for i in range(2):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx < N and 0 <= ny < M:
#       if board[nx][ny] == 1:
#         dfs(nx, ny, cnt + 1)
#       else:
#         dfs(nx, ny, cnt)

# dfs(0, 0, 0)
# print(max(result))

# dp이용해서 시간초과 해결
N, M = map(int, input().split())
board = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
dx = [0, 1]
dy = [1, 0]

dp = [[0] * (M + 1) for _ in range(N + 1)]

for row in range(1, N + 1):
  for col in range(1, M + 1):
    if board[row][col] == 1:
      dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + 1
    else:
      dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[N][M])