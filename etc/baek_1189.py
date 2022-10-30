# 2022/10/31 Baek 1189

R, C, K = map(int, input().split())
arr = []
for _ in range(R):
  arr.append(list(input()))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

result = 0
def dfs(x, y, depth):
  global result
  arr[x][y] = "T"
  if arr[0][C - 1] == "T":
    if depth == K:
      result += 1
    return
  else:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C:
        if arr[nx][ny] != "T":
          arr[nx][ny] = "T"
          dfs(nx, ny, depth + 1)
          arr[nx][ny] = "."

dfs(R - 1, 0, 1)
print(result)