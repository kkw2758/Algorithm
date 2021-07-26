# 2021/06/09 Baek 2839


# 일반적인 바텀업 방식의 dp 풀이
n = int(input())

dp = [5000] * (n + 1)
dp[0] = 0

def baek_2839(n):
    for i in [3,5]:
        for j in range(1, n + 1):
            dp[j] = min(dp[j], dp[j - i] + 1)

baek_2839(n)

if dp[n] == 5000:
    print(-1)
else:
    print(dp[n])

# 내가 생각하지 못한 풀이 -> greedy 알고리즘 이용
# 5kg 용량의 봉지를 가능한 최대한 많이 사용하면 Nkg을 포장하는대 필요한 봉지수를 최소화 할 수 있다.

n = int(input())

cnt = 0

while True:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break

    n -= 3
    cnt += 1

    if n < 0:
        print(-1)
        break