# n = int(input())

# arr = list(map(int, input().split()))

# dp = [1 for _ in range(n)]

# for i in range(1, n):
#   for j in range(i):
#     if arr[i] > arr[j]:
#       dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
# print(max(dp))


# import bisect

# n = int(input())
# arr = list(map(int, input().split()))

# dp = [arr[0]]

# for i in range(1, n):
#   if arr[i] > dp[-1]:
#     dp.append(arr[i])
#   else:
#     index = bisect.bisect_left(dp, arr[i])
#     dp[index] = arr[i]

# print(dp)
# print(len(dp))


# import bisect

# n = int(input())
# arr = list(map(int, input().split()))
# INF = 1e9
# dp = [0 for _ in range(n)]
# x = [INF for _ in range(n)]

# for i in range(n):
#   idx = bisect.bisect_left(x, arr[i])
#   x[idx] = arr[i]
#   dp[i] = idx + 1

# max_dp = max(dp)
# result = []


# print(dp)
# print(max_dp)
# for value in result:
#   print(value, end = " ")

import bisect

INF = int(2e9)
n = int(input())
arr = [0]
arr += list(map(int, input().split()))
dp = [0]
x = [-INF]

for i in range(1, n + 1):
  index = bisect.bisect_left(x, arr[i])
  dp.append(index)
  if len(x)  == index:
    x.append(arr[i])
  else:
    x[index] = arr[i]

max_dp = max(dp)
print(max_dp)

result = []
for i in range(n, 0, -1):
  if max_dp == 0:
    break
  if max_dp == dp[i]:
    result.append(arr[i])
    max_dp -= 1

# print(arr)
# print(dp)
# print(x)

result.reverse()
for value in result:
  print(value, end = " ")


# import bisect

# n = int(input())
# arr = list(map(int, input().split()))
# INF = 1e9
# dp = [0 for _ in range(n)]
# x = [INF for _ in range(n)]

# for i in range(n):
#   idx = bisect.bisect_left(x, arr[i])
#   x[idx] = arr[i]
#   dp[i] = idx + 1

# max_dp = max(dp)
# result = []
# target = max_dp

# for i in range(n-1, -1, -1):
#   if target == 0:
#     break  
#   if dp[i] == target:
#     result.append(arr[i])
#     target -= 1

# result.reverse()
# print(max_dp)
# for value in result:
#   print(value, end = " ")
    