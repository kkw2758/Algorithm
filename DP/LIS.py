# import bisect

# x = int(input())
# arr = list(map(int, input().split()))

# dp = [arr[0]]

# print(arr)

# for i in range(x):
#   print("arr[{}] = {}".format(i, arr[i]))
#   if arr[i] > dp[-1]:
#       dp.append(arr[i])
#   else:
#       idx = bisect.bisect_left(dp, arr[i])
#       dp[idx] = arr[i]
#       print(arr[i], dp)

# print(len(dp))
# print(dp)

# import bisect

# INF = 1e9
# n = int(input())
# arr = list(map(int, input().split()))
# dp = [1 for _ in range(n)]
# x = [INF for _ in range(n)]

# for i in range(n):
#   idx = bisect.bisect_left(x, arr[i])
#   x[idx] = min(x[idx], arr[i])
#   dp[i] = idx + 1

# max_dp = max(dp)
# # print(max(dp))
# print(dp)
# print(arr)

# result = []
# while max_dp in dp:
#   n = len(dp)
#   target = max_dp
#   temp = []
#   for i in range(n-1, -1, -1):
#     if target == 0:
#       break
#     if dp[i] == target:
#       if dp[i] == max_dp:
#         dp[i] = 0
#       temp.append(arr[i])
#       target -= 1
#   temp.reverse()
#   result.append(temp)

# print(result)

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