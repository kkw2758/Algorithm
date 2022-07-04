# 2022/06/06 Baek 18353

# import bisect

# n = int(input())
# arr = list(map(int, input().split()))
# arr.reverse()

# dp = [arr[0]]
# for i in range(1,n):
#   idx = bisect.bisect_left(dp, arr[i])
#   if idx == len(dp):
#     dp.append(arr[i])
#   else:
#     dp[idx] = min(dp[idx], arr[i])

# print(n - len(dp))


n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))