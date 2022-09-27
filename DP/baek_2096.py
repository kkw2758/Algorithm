# 2022/09/27 Baek 2096

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0,0,0]]
for _ in range(n):
  graph.append(list(map(int, input().rstrip().split())))

max_temp = [member for member in graph[0]]
min_temp = [member for member in graph[0]]
max_dp = [0,0,0]
min_dp = [0,0,0]

for i in range(1, n + 1):
  for j in range(3):
    max_value = max_temp[j]
    min_value = min_temp[j]
    for k in [-1, 1]:
      if 0 <= j + k <= 2:
        max_value = max(max_value, max_temp[j + k])
        min_value = min(min_value, min_temp[j + k])
    max_dp[j] = max_value + graph[i][j]
    min_dp[j] = min_value + graph[i][j]
  
  max_temp = [member for member in max_dp]
  min_temp = [member for member in min_dp]

print(max(max_dp), min(min_dp))

# 인터넷 참고 코드
# https://kyun2da.github.io/2021/04/27/goDown/

import sys
input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
  a, b, c = map(int, input().split())
  for j in range(3):
    if j == 0:
      max_tmp[j] = a + max(max_dp[j], max_dp[j + 1])
      min_tmp[j] = a + min(min_dp[j], min_dp[j + 1])
    elif j == 1:
      max_tmp[i] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
      min_tmp[i] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
    else:
      max_tmp[i] = c + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
      min_tmp[i] = c + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])

  for j in range(3):
    max_dp[j] = max_tmp[j]
    max_dp[j] = min_tmp[j]

print(max(max_dp), min(min_dp))