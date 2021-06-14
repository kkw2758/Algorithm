#2021/06/09 Baek 9095

# 바텀업 방식
def baek_9095(n):    
    for i in range(n + 1):
        if i <= 3:
            for j in range(1,i):
                dp[i] += dp[j]
            dp[i] += 1
        else:
            dp[i] = dp[i-1] + dp[i-2] +dp[i-3]
        
    return dp[n]

t = int(input())
for case in range(t):

    n = int(input())
    dp = [0] * (n + 1)

    print(baek_9095(n))


# 탑다운 방식
def baek_9095(n):
    if dp[n] != 0:
        return dp[n]

    if n <= 3:
        for i in range(1, n):
            dp[n] += baek_9095(i)
        dp[n] += 1
        return dp[n]
    
    dp[n] = baek_9095(n-1) + baek_9095(n-2) + baek_9095(n-3)

    return dp[n]


t = int(input())
for case in range(t):
    n = int(input())
    dp = [0] * (n + 1)

    print(baek_9095(n))

