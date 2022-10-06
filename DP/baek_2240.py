# 2022/10/06 Baek 2240

T, W = map(int, input().split())
table = [0]
for _ in range(T):
    table.append(int(input()))

dp = [[0] * (T + 1) for _ in range(W + 1)]

for i in range(1, T + 1):
    if table[i] == 1:
        dp[0][i] = dp[0][i - 1] + 1
    else:
        dp[0][i] = dp[0][i - 1]


for i in range(1, W + 1):
    for j in range(i, T + 1):
        if i % 2 == 0:  # 짝수 >>> 1이 되야함
            if table[j] == 2:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
        else:           # 홀수 >>> 2가 되야함
            if table[j] == 1:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1


print(dp[-1][-1])