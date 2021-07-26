# 2021/06/24 Baek 9461

import sys
read = sys.stdin.readline

t = int(read())
cases = []

for i in range(t):
    n = cases.append(int(read()))

max_n = max(cases)
dp = [0] * (max_n + 1)

dp[1] = 1

for i in range(2, max_n + 1):
    if i == 2:
        dp[i] = 1
    else:
        dp[i] = dp[i-2] + dp[i-3]

for case in cases:
    print(dp[case])
    