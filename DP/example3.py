'''
<바닥 공사>
가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다.
태일이는 이 얇은 바닥을 1 x 2의 덮개, 2 x 1의 덮개, 2 x 2의 덮개를 이용해 채우고자 한다.
이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어 2 x 3 크기의 바닥을 채우는 경우의 수는 5가지이다.

입력조건
첫쨰 줄에 N이 주어진다. (1 <= N <= 1,000)

출력 조건
첫쨰 줄에 2 x N 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력한다.
'''

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i-2] * 2) % 796796

print(dp[n])


n = int(input())
dp = [0] *(n + 1)


#--------------------복습---------------------
def bottom_up(n):
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + 2 * dp[i-2]) % 796796

bottom_up(n)
print(dp[n])

n = int(input())
dp = [0] * (n + 1)

def top_down(n):
    if n == 1:
        dp[n] = 1
        return
    if n == 2:
        dp[n] = 3
    
    if dp[n] != 0:
        return
    
    top_down(n-2)
    top_down(n-1)
    dp[n] = dp[n-1] + 2 * dp[n-2]
    return

top_down(n)
print(dp[n])