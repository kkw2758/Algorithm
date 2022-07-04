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
    