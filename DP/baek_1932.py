# 2021/06/13 Baek 1932

import sys

read = sys.stdin.readline

n = int(read())
triangle = []

for i in range(n):
    triangle.append(list(map(int, read().strip().split())))

dp = []
for i in range(n):
    dp.append([0] * (i + 1))

def solution(n, dp, triangle):
    dp[0][0] = triangle[0][0]

    for i in range(n - 1):
        #member_cnt = i + 1
        for j in range(i + 1):
            for k in range(2):
                dp[i+1][j + k] = max(dp[i+1][j + k], dp[i][j] + triangle[i + 1][j + k])


solution(n, dp, triangle)
print(max(dp[n-1]))