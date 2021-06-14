# 2021/06/13 Baek 2579

# n이 1일때를 고려하지않아서 index에러 났음..
# 문제 해결이힘들때는 그림으로 표현해서 생각해보자

import sys
read = sys.stdin.readline

n = int(read().strip())
s = []
dp = [0] * n

for i in range(n):
    s.append(int(read().strip()))

for i in range(n):

    if i == 0:
        dp[0] = s[0]
    elif i == 1:
        dp[1] = s[0] + s[1]
    elif i == 2:
        dp[2] = max(s[0] + s[2], s[1] + s[2])
    else:
        dp[i] = max(dp[i-2] + s[i], dp[i-3] + s[i-1] + s[i])

print(dp[n-1])



# L[i][0] -> i - 1 번쨰 계단을 밟았을 때 최댓값.
# L[i][1] -> i - 2 번쨰 계단을 밟았을 때 최댓값.
import sys
read = sys.stdin.readline

n = int(read().strip())
L = []

for i in range(n):
    L.append(int(read()))

if n == 1:
    print(L[0])
else:
    L[0] = [L[0], L[0]]
    L[1] = [L[0][0] + L[1], L[1]]

    for i in range(2, n):
        L[i] = [L[i] + L[i-1][1], L[i] + max(L[i-2])]

print(max(L[n-1]))