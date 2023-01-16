# 2023/01/16 Baek 1890
import time
# 첫번째 방법 시작점으로부터 직접 점프하면서 모든 경우의수 찾아봤음 - 시간 초과
# dfs로 하니까 시간초과
N = int(input())
board = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
# 오른쪽 아래
dx = [0, 1]
dy = [1, 0]

stack = [(0, 0)]
dp[0][0] = 1
start = time.time()
while stack:
  x, y = stack.pop()
  if board[x][y] == 0:
    continue
  number = board[x][y]
  
  for i in range(2):
    nx = x + dx[i] * number
    ny = y + dy[i] * number

    if 0 <= nx < N and 0 <= ny < N:
      dp[nx][ny] += dp[x][y]
      stack.append((nx, ny))
end = time.time()
print(dp[-1][-1])


# 2차원 배열 board를 순회하면서 진행 > 시간복잡도 O(N^2)
# 4 <= N <= 100 이고 시간제한이 1초이므로 100 ^^ 2 = 10000 이므로 충분히 시간내 통과 가능
# dp[i][j]에는 (i, j)에 도달할 수 있는 경우의 수를 담음
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dp[0][0] = 1
for i in range(N):
  for j in range(N):
    # 이 조건이 없으면  (i, j) == (N - 1, N - 1)일때도 밑의 내용이 실행됨
    # board[N - 1][N - 1]의 값이 0 이므로 dp[N - 1][N - 1] 값이 여러번 더해진다.
    # 테스트 케이스에서는 dp[i][j] = 3, dp[i][j] = 6, dp[i][j] = 12 
    if i == N - 1 and j == N - 1:
      print(dp[i][j])
      break

    if i + board[i][j] < N:
      dp[i + board[i][j]][j] += dp[i][j]
    if j + board[i][j] < N:
      dp[i][j + board[i][j]] += dp[i][j]