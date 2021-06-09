# 2021/06/09 Baek 1003

def dynamic_fibo(n):
    if dp[n]:
        return dp[n]

    if n == 0:
        dp[n] = (1,0)
        return dp[n]
    elif n == 1:
        dp[n] = (0,1)
        return dp[n]

    zero_cnt = dynamic_fibo(n-1)[0] + dynamic_fibo(n-2)[0]
    one_cnt = dynamic_fibo(n-1)[1] + dynamic_fibo(n-2)[1]

    dp[n] = (zero_cnt, one_cnt)

    return dp[n]

t = int(input())

for case in range(t):
    n = int(input())
    dp = [()] * (n + 1)
    result = dynamic_fibo(n)
    print(result[0],result[1])
