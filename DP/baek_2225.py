# 2022/09/26 Baek 2225

n, k = map(int, input().split())

# dp[i][j] > i개를 이용해서 j개를 만드는 경우의 수
dp = [[1] * (n + 1) for _ in range(k + 1)]


for i in range(2, k + 1):
  for j in range(1, n + 1):
    result = 0
    for w in range(j + 1):
      result += dp[i - 1][w] * dp[1][j - w]
    dp[i][j] = result

print(dp[k][n] % 1000000000)