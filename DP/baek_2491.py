# 2022/09/25 Baek 2491

N = int(input())
ary = list(map(int, input().split()))

ascending_dp = [1] * N
descending_dp = [1] * N

for i in range(1, N):
  if ary[i - 1] <= ary[i]:
    ascending_dp[i] =  ascending_dp[i - 1] + 1
  
  if ary[i - 1] >= ary[i]:
    descending_dp[i] = descending_dp[i - 1] + 1

ascending_result = max(ascending_dp)
descending_result = max(descending_dp)

if ascending_result > descending_result:
  print(ascending_result)
else:
  print(descending_result)