# 2023/05/03 Baek 11444

# 시간제한 1초
# 메모리 제한 256MB
# n번째의 피보나치 수를 구하는 문제이다.
# n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.
# 근데 n이 너무크다.

# 일반 적인 dp 로접근 -> n의 크기 만큼의 배열을 선언하면 메모리 에러가 날 것이다.
# 어떻게 메모리 에러 방지를 할까? -> 딕셔너리로 메모리 절약은 모르겠는데 시간은 줄어들것

import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
dp = dict()

def fibo(n):
    if n in dp:
        return dp[n]
    if n == 0:
        dp[n] = 0
        return dp[n]
    elif n == 1:
        dp[n] = 1
        return dp[n]
    
    dp[n] = (fibo(n - 1) + fibo(n-2))%1000000007
    return dp[n]

print(fibo(n))

# 참고 풀이 1
# 참고 : https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11444-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-6-%EA%B3%A8%EB%93%9C3-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5
import sys
input = sys.stdin.readline

n = int(input())
p = 1000000007

# n번 째 피보나치 수는 행렬 (1 1, 1 0)^n 의 1행 2열 값이다(단, n>=1일때)

# A 행렬과 B 행렬의 곱을 리턴하는 함수
def mul(A, B):
    n = len(A)
    Z = [[0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col]
            Z[row][col] = e % p
            
    return Z

# 입력받은 A 메트릭스를 분할정복 방법을 이용해서 k 제곱하는 함수
def square(A, k):
    if k == 1:
        for row in range(len(A)):
            for col in range(len(A)):
                A[row][col] %= p
        return A
    
    tmp = square(A, k // 2)
    if k % 2 == 1:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    
fib_matrix = [[1, 1], [1, 0]]
print(square(fib_matrix, n)[0][1])


# 참고 풀이 2
# 참고 : https://ku-hug.tistory.com/122
dp = dict()

def fibo(n):
      if dp.get(n) != None:
            return dp[n]
      if n == 0:
            return 0
      if n == 1 or n == 2:
            return 1
      if n % 2 == 0:
            dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000007 # 맨 처음에는 % 1000000007을 해주지 않아 시간초과가 났었다..
            dp[n // 2 - 1] = fibo(n // 2 - 1) % 1000000007
            return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
      else:
            dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000007
            dp[n // 2] = fibo(n // 2) % 1000000007
            return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2

print(fibo(int(input())) % 1000000007)