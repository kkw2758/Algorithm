import bisect

n = int(input())
arr = list(map(int, input().split()))
D = [1 for _ in range(n)]
dp = [arr[0]]

for i in range(1, n):
  if arr[i] > dp[-1]:
    D[i] = len(dp) + 1
    dp.append(arr[i])
  else:
    idx = bisect.bisect_left(dp, arr[i])
    dp[idx] = arr[i]
    D[i] = idx + 1

max_dp = max(D)
result = []
target = max_dp

for i in range(n-1, -1, -1):
  if target == 0:
    break  
  if D[i] == target:
    result.append(arr[i])
    target -= 1

result.reverse()
print(max_dp)
for value in result:
  print(value, end = " ")