#bottom_up
# n = int(input())
# arr = []

# for i in range(n):
#   arr.append(list(map(int, input().split())))

# dp = [[0] * i for i in range(1, n + 1)]

# dp[0][0] = arr[0][0]
# for row in range(1, n):
#   for col in range(row + 1):
#     if col > row - 1:
#       up_right = 0
#     else:
#       up_right = dp[row - 1][col]
#     if col - 1 < 0:
#       up_left = 0
#     else:
#       up_left = dp[row - 1][col - 1]

#     dp[row][col] = arr[row][col] + max(up_left, up_right)

# print(max(dp[n - 1]))

n = int(input())

triangle = []
for _ in range(n):
  triangle.append(list(map(int, input().split())))

dp = [[-1] * (i + 1) for i in range(n)]

def top_down(row, col):
  if dp[row][col] != -1:
    return dp[row][col]
  
  if row == 0:
    dp[row][col] = triangle[0][0]
    return dp[row][col]

  if col == 0:
    dp[row][col] = top_down(row - 1, col) + triangle[row][col]
  elif col == row:
    dp[row][col] = top_down(row - 1, col - 1) + triangle[row][col]
  else:
    dp[row][col] = max(top_down(row - 1, col), top_down(row - 1, col - 1)) + triangle[row][col]

  return dp[row][col]

result = 0
for i in range(n):
  result = max(result, top_down(n - 1, i))

print(result)