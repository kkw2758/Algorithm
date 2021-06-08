'''
<효율적인 화폐 구성>
N가지 종류의 화폐가 있따. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.

입력 조건
첫쨰 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10,000)
이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.

출력 조건
첫째 줄에 M원을 만들기 위한 최소환의 화폐 개수를 출력한다.
불가능할 때는 -1을 출력한다.
'''

#나의 풀이
n, m = map(int, input().split())
dp = [10001] * (m + 1)
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

#coin_list.sort()
for i in range(1, m + 1):
    for coin in coin_list:
        if i - coin == 0:
            dp[i] = 1
            break
        if i - coin > 0:
            dp[i] = min(dp[i], dp[i-coin] + 1)


if dp[m] != 10001:
    print(dp[m])
else:
    print(-1)


n, m = map(int, input().split())
dp = [10001] * (m + 1)
dp[0] = 0
array = []
for x in range(n):
    array.append(int(input()))

for i in range(n):
    for j in range(array[i], m + 1):
        dp[j] = min(dp[j], dp[j - array[i]] + 1)


if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])