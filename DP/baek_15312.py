# 2022/09/24 Baek 15312

A = input()
B = input()

alpha_dict = {}
alpha_info = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
for i in range(26):
  alpha_dict[chr(65 + i)] = alpha_info[i]

dp = [[] for _ in range(len(A) * 2 - 1)]

for i in range(len(A)):
  dp[0].append(alpha_dict[A[i]])
  dp[0].append(alpha_dict[B[i]])

for i in range(1, len(A) * 2 - 1):
  for j in range(len(dp[i - 1]) - 1):
    dp[i].append(int(str(dp[i - 1][j] + dp[i - 1][j + 1])[-1]))

print("{}{}".format(dp[-1][0],dp[-1][1]))