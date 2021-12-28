'''
<개미전사>
개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 한다.
메뚜기 마을에는 여러 개의 식량창고가 있는데 식량창고는 일직선으로 이어져있다.
각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 젓는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정이다.
이때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.
따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
개미 전사는 식량창고가 이렇게 일직선상일 때 최대한 많은 식량을 얻기를 원한다.
개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 떄 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.

입력 조건
첫째 줄에 식량창고의 개수 N이 주어진다. (3 <= N <= 100)
둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다. (0 <= K <= 1,000)

출력 조건
첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.
'''

# 나의 풀이
n = int(input())
array = list(map(int, input().split()))
dp  = [0] * 101


def solve(n):
    dp[1] = array[n-1]
    cnt = 2
    for i in range(n-2, -1, -1):
        dp[cnt] = max(dp[cnt-1], array[i] + dp[cnt-2])
        cnt += 1

solve(n)
print(dp[n])


# 해설 풀이
n = int(input())
array = list(map(int,input().split()))
dp = [0] * 100
dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], array[i] + dp[i-2])

print(dp[n - 1])


#--------------------복습---------------------
n = int(input())
array = list(map(int, input().split()))
dp = [0] * (n + 1)

def bottop_up(array):
    n = len(array)
    dp[1] = array[-1]
    dp[2] = max(array[-1], array[-2])

    for i in range(3, n + 1):
        dp[i] = max(array[-i] + dp[i-2], dp[i-1])

bottop_up(array)
print(dp[n])

n = int(input())
array = list(map(int, input().split()))
dp = [0] *(n + 1)

def top_down(n):
    if n == 1:
        dp[n] = array[-1]
        return
    if n == 2:
        dp[n] = max(array[-1], array[-2])
        return
    if dp[n] != 0:
        return

    top_down(n-2)
    top_down(n-1)
    dp[n] = max(array[-n] + dp[n-2], dp[n-1])
    return

top_down(n)
print(dp)
print(dp[n])

    