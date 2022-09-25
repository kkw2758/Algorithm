# 2022/09/25 Baek 2293

INF = int(1e9)
n, k = map(int, input().split())
ary = []

for _ in range(n):
  ary.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1
for i in range(len(ary)):
  for j in range(ary[i], k + 1):
    dp[j] += dp[j - ary[i]] 

print(dp[-1])