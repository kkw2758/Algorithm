import bisect

n = int(input())
arr = list(map(int, input().split()))
INF = 1e9
dp = [0 for _ in range(n)]
x = [INF for _ in range(n)]

for i in range(n):
  idx = bisect.bisect_left(x, arr[i])
  x[idx] = arr[i]
  dp[i] = idx + 1

max_dp = max(dp)
result = []
target = max_dp

for i in range(n-1, -1, -1):
  if target == 0:
    break  
  if dp[i] == target:
    result.append(arr[i])
    target -= 1

result.reverse()
print(max_dp)
for value in result:
  print(value, end = " ")



# import bisect

# N = int(input())
# arr = list(map(int, input().split()))
# dp = [arr[0]]

# for i in range(1, N):
#   if arr[i] > dp[-1]:
#     dp.append(arr[i])
#   else:
#     idx = bisect.bisect_left(dp, arr[i])
#     dp[idx] = arr[i]

# print(len(dp))
# for i in range(len(dp)):
#   print(dp[i], end = " ")
