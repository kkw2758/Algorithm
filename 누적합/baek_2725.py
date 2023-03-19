# 2023/03/20 Baek 2725
# https://sangminlog.tistory.com/entry/boj-2725
# (0,0) 에서 보이지 않으려면 직선의 기울기가 달라야 한다.
# 분자와 분모의 최대공약수가 1인 값들을 찾아내면 된다.

def gcd(i, j):
    if j == 0:
        return i
    return gcd(j, i % j)

dp = [0 for _ in range(1001)]
dp[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i == j:
            continue

        if gcd(i, j) == 1:
            cnt += 2
    dp[i] = dp[i-1] + cnt


T = int(input())
for _ in range(T):
    N = int(input())

    print(dp[N])