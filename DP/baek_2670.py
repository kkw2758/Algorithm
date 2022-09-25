# 2022/09/25 Baek 2670

# N = int(input())

# dp = [[0] * (N + 1) for _ in range(N + 1)]
# for i in range(1, N + 1):
#   dp[1][i] = float(input())


# max_value = 0
# for i in range(2, N + 1):
#   for j in range(i, N + 1):
#     dp[i][j] = dp[i - 1][j - 1] * dp[1][j]
#     max_value = max(max_value, dp[i][j])

# print("{:.3f}".format(max_value))

N = int(input())
dp = [0]
for _ in range(N):
  dp.append(float(input()))

for i in range(2, N + 1):
  dp[i] = max(dp[i], dp[i] * dp[i - 1])

print("{:.3f}".format(max(dp)))