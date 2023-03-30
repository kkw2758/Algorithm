# 2023/03/29 Baek 5549

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
dp = [[[0, 0, 0] for _ in range(M + 1)] for _ in range(N + 1)]

map_info = [[0] * (M + 1)]
for _ in range(N):
    map_info.append([0] + list(input().strip()))


for i in range(1, N + 1):
    for j in range(1, M + 1):
        for k in range(3):
            dp[i][j][k] += dp[i - 1][j][k] + dp[i][j - 1][k] - dp[i - 1][j - 1][k]
        
        if map_info[i][j] == "J":
            dp[i][j][0] += 1
        elif map_info[i][j] == "O":
            dp[i][j][1] += 1
        elif map_info[i][j] == "I":
            dp[i][j][2] += 1


for _ in range(K):
    a, b, c, d = list(map(int, input().split()))
    for i in range(3):
        print(dp[c][d][i] - dp[a - 1][d][i] - dp[c][b - 1][i] + dp[a - 1][b - 1][i], end = " ")
    print()