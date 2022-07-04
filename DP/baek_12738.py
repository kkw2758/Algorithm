import bisect

n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]
for x in range(n):
  idx = bisect.bisect_left(dp, arr[x])
  if idx == len(dp):
    dp.append(arr[x])
  else:
    dp[idx] = arr[x]

print(len(dp))