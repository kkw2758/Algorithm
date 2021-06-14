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

# 다른 사람의 풀이
# 이풀이에서는 입력받은 테스트케이스의 값중 가장 큰 수에 대해서만 dp 테이블을 생성하면 나머지 테스트 케이스의 dp 테이블을 따로 만들 필요가 없다는 점을 이용하여 효율적
import sys
t = int(input())
dp = [[1,0], [0,1]]
q = [int(sys.stdin.readline()) for _ in range(t)]

for i in range(2, max(q) + 1):
    dp.append([dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]])

print(dp)

for i in q:
    print(dp[i][0], dp[i][1])