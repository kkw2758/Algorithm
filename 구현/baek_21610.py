#2022/10/19 baek 21610
# [i, j] not in cloud 시간 오래걸림
import sys
input = sys.stdin.readline

def water_copy_bug(cloud):
  for x, y in cloud:
    cnt = 0
    for i in [1, 3, 5, 7]:
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if arr[nx][ny] != 0:
          cnt += 1

    arr[x][y] += cnt

def solution():
  cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
  for _ in range(m):
    d, s = map(int, input().split())
    cloud = [[(x + dx[d - 1] * s) % n, (y + dy[d - 1] * s) % n] for x, y in cloud]
    for x, y in cloud:
      arr[x][y] += 1
    water_copy_bug(cloud)
    new_cloud = []
    for i in range(n):
      for j in range(n):
        if arr[i][j] >= 2 and [i, j] not in cloud:
          arr[i][j] -= 2
          new_cloud.append([i, j])
    cloud = new_cloud
    
n, m = map(int, input().split())
arr = []

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(n):
  arr.append(list(map(int, input().split())))

solution()
result = 0
for i in range(n):
    result += sum(arr[i]) 

print(result)


#2022/10/19 baek 21610
# 없어진 구름인지 검사하는 여부 visited[i][j] == False
# 훨씬 빠름
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

arr = [list(map(int, input().split())) for _ in range(n)]
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

for _ in range(m):
  d, s = map(int, input().split())
  next_cloud = []
  for c in cloud:
    x = c[0]
    y = c[1]
    nx = (x + dx[d - 1] * s) % n
    ny = (y + dy[d - 1] * s) % n
    next_cloud.append([nx, ny])

  visited = [[False]*n for _ in range(n)]
  for x, y in next_cloud:
    arr[x][y] += 1
    visited[x][y] = True

  cloud = []

  for x, y in next_cloud:
    cnt = 0
    for i in range(1, 8, 2):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] >= 1:
        cnt += 1

    arr[x][y] += cnt

  for i in range(n):
    for j in range(n):
      if arr[i][j] >= 2 and visited[i][j] == False:
        arr[i][j] -= 2
        cloud.append([i, j])
    
result = 0
for i in range(n):
    result += sum(arr[i]) 

print(result)