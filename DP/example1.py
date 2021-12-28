'''
<1로 만들기>
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
1. X가 5로 나누어 떨어지면, 5로 나눈다.
2. X가 3으로 나누어 떨어지면, 3으로 나눈다.
3. X가 2로 나누어 떨어지면, 3으로 나눈다.
4. X에서 1을 뺀다.

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력조건
첫째 줄에 정수X가 주어진다. (1 <= X <= 30,000)

출력조건
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''

'''
#나의 풀이
dp = [0] * 30001

def example1(x):
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 1

    for i in range(6,x + 1):
        temp = 30000    #임의의 최댓값

        if i % 5 == 0:
            temp = min(temp, 1 + dp[i//5])
        if i % 3 == 0:
            temp = min(temp, 1 + dp[i//3])
        if i % 2 == 0:
            temp = min(temp, 1 + dp[i//2])
        
        temp = min(temp, 1 + dp[i-1])

        dp[i] = temp

x = int(input())
example1(x)
print(dp[x])
'''


#해설의 풀이
x = int(input())
dp = [0] * 30001

def example1(x):
    for i in range(2, x + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i//5] + 1)

        
example1(x)
print(dp[x])

#--------------------복습---------------------
import sys
sys.setrecursionlimit(1000000)

n = int(input())
dp = [0] * 30001

def top_down(n):
    if n == 1:
        return 0
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = top_down(n-1) + 1
    
    if n % 2 == 0:
        dp[n] = min(dp[n], top_down(n//2) + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], top_down(n//3) + 1)
    if n % 5 == 0:
        dp[n] = min(dp[n], top_down(n//5) + 1)
    
    return dp[n]

print(top_down(n))


n = int(input())
dp = [0] * 30001

def top_down2(n):
    if n == 1:
        return
    
    if dp[n] != 0:
        return
    top_down2(n-1)
    dp[n] = dp[n-1] + 1
    
    if n % 2 == 0:
        dp[n] = min(dp[n], dp[n//2] + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], dp[n//3] + 1)
    if n % 5 == 0:
        dp[n] = min(dp[n], dp[n//5] + 1)
    

top_down2(n)
print(dp[n])