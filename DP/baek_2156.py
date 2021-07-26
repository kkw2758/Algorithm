# 2021/06/22 Baek 2156

import sys

read = sys.stdin.readline

n = int(read())
array = []
for _ in range(n):
    array.append(int(read()))

dp = [0] * (n + 1)
dp[1] = array[0]

for i in range(2, n + 1):
    if i == 2:
        dp[i] = array[0] + array[1]
    else:
        case1 = dp[i-1]
        case2 = array[i-1] + dp[i-2]
        case3 = array[i-1] + array[i-2] + dp[i-3]

        dp[i] = max(case1, case2, case3)

print(dp[-1])