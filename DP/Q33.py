n = int(input())

ary = []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
  ary.append(list(map(int, input().split())))

for i in range(1, n + 1):
  t, p = ary[i - 1]
  
  if i + t - 1 > n:
    continue

  for j in range(i + t - 1, n + 1):
    dp[j] = max(dp[j], dp[i - 1] + p)
  # print(i, dp)
print(dp[n])