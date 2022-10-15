# 2022/10/03 Baek 2059

N = int(input())
ary = [[]]
for _ in range(N):
  ary.append(list(map(int, input().split())))

dp = [0] * (N + 1)

for i in range(1, N + 1):
  if ary[i][1] == 0:
    dp[i] = ary[i][0]
  else:
    for j in range(1, ary[i][1] + 1):
      dp[i] = max(dp[i], dp[ary[i][1 + j]] + ary[i][0])
  # print(dp)
print(max(dp))