# 2021/06/25 Baek 14501

import sys
read = sys.stdin.readline

n = int(read())
table = [[0, 0]]

for _ in range(n):
    table.append(list(map(int, read().strip().split())))

dp = [0] * (n + 5)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i-1])
    dp[i + table[i][0] - 1] = max(dp[i + table[i][0] - 1], dp[i-1] + table[i][1])
    #print("i = {}\n{}".format(i,dp))

print(dp[n])