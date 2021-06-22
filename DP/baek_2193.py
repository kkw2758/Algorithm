# 2021/06/22 baek 2193

import sys
read = sys.stdin.readline

n = int(read())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n])