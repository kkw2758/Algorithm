# 2021/06/28 Baek 11052


# 나의 풀이
# 푸는데 오류는 없었지만 안해도되는 연산을 많이 반복해서 시간이 오래걸림
import sys

read = sys.stdin.readline

n = int(read())
p_array = list(map(int, read().strip().split()))

dp = [0] * (n+1)

for i in range(n):
    value = p_array[i]
    for j in range(i+1, n + 1):
        dp[j] = max(dp[j], dp[j-(i + 1)] + value)

print(dp[n])



import sys

read = sys.stdin.readline

n = int(read())
card = [0]
card += list(map(int, read().strip().split()))

dp = [0] * (n+1)
dp[1] = card[1]

for i in range(2, n + 1):
    dp[i] = card[i]
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[n])



import sys

read= sys.stdin.readline

n = int(read())
card = [0]
card += list(map(int, read().strip().split()))

dp = [0] * (n + 1)
dp[1] = card[1]

for i in range(2, n+1):
    for j in range(1,i + 1):
        dp[i] = max(dp[i], dp[i-j] + card[j])

print(dp[n])