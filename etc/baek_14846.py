# 2022/12/19 Baek 14486

# # 시간 초과
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# def query(x1, y1, x2, y2):
#   result_set = set()
#   for row in range(x1, x2 + 1):
#     for col in range(y1, y2 + 1):
#       result_set.add(board[row][col])

#   return len(result_set)

# Q = int(input())
# for i in range(Q):
#   x1, y1, x2, y2 = map(int, input().split())
#   print(query(x1 - 1, y1 - 1, x2 - 1, y2 - 1))

# dp 이용, 누적합
import sys
input = sys.stdin.readline

N = int(input())
array = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 10 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
  for j in range(1, N + 1):
    for k in range(1, 10):
      if k == array[i][j]:
        dp[i][j][k] += 1
      dp[i][j][k] += dp[i - 1][j][k] + dp[i][j - 1][k] - dp[i - 1][j - 1][k]

Q = int(input())
for _ in range(Q):
  x1, y1, x2, y2 = map(int, input().split())
  cnt = 0
  for k in range(1, 10):
      if dp[x2][y2][k] - dp[x2][y1 - 1][k] - dp[x1-1][y2][k] + dp[x1-1][y1-1][k]:
        cnt += 1
  print(cnt)