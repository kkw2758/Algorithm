# 2021/06/13 Baek 10870

def top_down_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return top_down_fibo(n-1) + top_down_fibo(n-2)

n = int(input())
print(top_down_fibo(n))


n = int(input())
dp = [0] * (n + 1)
def bottom_up_fibo(n):
    if n >= 1:
        dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

bottom_up_fibo(n)
print(dp[n])


# simple solution
def simple_solution(n):
    x = 0
    y = 1
    for i in range(n):
        x, y = y, x + y
    
    return x

n = int(input())
print(simple_solution(n))