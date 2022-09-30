# 2022/09/30 Baek 5557

n = int(input())
ary = [0] + list(map(int, input().split()))
target = ary[-1]
ary = ary[:-1]

dp = [[0] * 21 for _ in range(n)]
dp[1][ary[1]] = 1 

for i in range(2, len(ary)):
  for j in range(21):
    if dp[i - 1][j]: #i - 1개로 만들 수 있다면
      if 0 <= j + ary[i] <= 20:
        dp[i][j + ary[i]] += dp[i - 1][j]

      if 0 <= j - ary[i] <= 20:
        dp[i][j - ary[i]] += dp[i - 1][j]


print(dp[-1][target])