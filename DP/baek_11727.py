# 2021/06/24 Baek 11727

import sys
read = sys.stdin.readline

n = int(read())

dp = [0] * (n + 1)

dp[1] = 1

for i in range(2, n+1):
    if i == 2:
        dp[i] = 3
        continue
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n] % 10007)