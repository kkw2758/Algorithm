# 2022/09/22 Baek 17202

A = list(map(int, list(input())))
B = list(map(int, list(input())))
dp = [[] for _ in range(15)]

for i in range(8):
  dp[0].append(A[i])
  dp[0].append(B[i])


for i in range(1, 15):
  for j in range(len(dp[i - 1]) - 1):
    value = dp[i - 1][j] + dp[i - 1][j + 1]
    value = int(str(value)[-1])
    dp[i].append(value)

print(str(dp[14][0]) + str(dp[14][1]))