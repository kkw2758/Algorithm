t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))

  graph = [ [ i for i in arr[j * m : (j + 1) * m]] for j in range(n)]
  dp = [ [0] * m for i in range(n)]

  for i in range(n):
    dp[i][0] = graph[i][0]

  for col in range(1, m):
    for row in range(n):
      if row == 0:
        dp[row][col] = graph[row][col] + max(dp[row][col - 1], dp[row + 1][col - 1])
      elif row == n - 1:
        dp[row][col] = graph[row][col] + max(dp[row][col - 1], dp[row - 1][col - 1])
      else:
        dp[row][col] = graph[row][col] + max(dp[row][col - 1], dp[row - 1][col - 1], dp[row + 1][col - 1])
    
  result = 0
  for row in range(n):
    if result < dp[row][m - 1]:
      result = dp[row][m - 1]

  print(result)