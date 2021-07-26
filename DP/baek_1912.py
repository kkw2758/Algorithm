# 2021/06/21 Baek 1912

import sys
read = sys.stdin.readline

n = int(input())
array = list(map(int, read().strip().split()))

dp = [-1001] * n
dp[0] = array[0]
for i in range(1, n):
    if dp[i-1] > 0 :
        dp[i] = array[i] + dp[i - 1]
    else:
        dp[i] = array[i]
    #dp[i] = max(array[i], array[i] + dp[i - 1])

print(max(dp))



import sys
read = sys.stdin.readline

n = int(read())
array = list(map(int, read().strip().split()))

for i in range(1, n):
    if array[i - 1] > 0 :
        array[i] = array[i - 1] + array[i]

print(max(array))