# 2022/12/05 Baek 1941
# N x N 2차원 행렬을 1차원으로 펴서 생각하는 아이디어
# 해당 문제에서는 5x5 2차원 행렬을 크기 25인 1차원 행렬로 생각하여
# 25개의 인덱스 값중 7 개를 뽑아서 처리한다.
# 뽑은 값을 idx 이라고하면 row(행) = idx // 5, col(열) = idx % 5
# idx = row * 5 + col

from collections import deque

student_arr = [list(input()) for _ in range(5)]
# 일단 7 명 뽑고 학생확인
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

arr = []


def dfs(arr):
  visited = [[1] * 5 for _ in range(5)]
  for x, y in arr:
    visited[x][y] = 0
  stack = []
  stack.append((arr[0][0], arr[0][1]))
  visited[arr[0][0]][arr[0][1]] = 1
  cnt = 1
  while stack:
    x, y = stack.pop()
    for idx in range(4):
      nx = x + dx[idx]
      ny = y + dy[idx]
      if 0 <= nx < 5 and 0 <= ny < 5:
        if visited[nx][ny] == 0 and (nx, ny) in arr:
          cnt += 1
          visited[nx][ny] = 1
          stack.append((nx, ny))

  if cnt == 7:
    return True
  else:
    return False

def bfs(arr):
  visited = [[1] * 5 for _ in range(5)]
  for x, y in arr:
    visited[x][y] = 0
  q = deque()
  q.append((arr[0][0], arr[0][1]))
  visited[arr[0][0]][arr[0][1]] = 1
  cnt = 1

  while q:
    x, y = q.popleft()
    for idx in range(4):
      nx = x + dx[idx]
      ny = y + dy[idx]
      if 0 <= nx < 5 and 0 <= ny < 5:
        if visited[nx][ny] == 0 and (nx, ny) in arr:
          visited[nx][ny] = 1
          cnt += 1
          q.append((nx, ny))
  
  if cnt == 7:
    return True
  else:
    return False

result = 0
def backtracking(depth, start, Y_cnt):
  global result
  if Y_cnt >= 4 or 25 - start < 7 - depth:
    return
  if depth == 7:
    if dfs(arr):
      result += 1
    return

  for i in range(start, 25):
    x = i % 5
    y = i // 5
    arr.append((x, y))
    backtracking(depth + 1, i + 1, Y_cnt + (student_arr[x][y] == "Y"))
    arr.pop()

backtracking(0, 0, 0)
print(result)

#---------------------------------------------
arr = [input() for _ in range(5)]
ans = 0
p = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0] * 5 for _ in range(5)]

def check(S):
  global visit
  x = S // 5
  y = S % 5

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < 5 and 0 <= ny < 5:
      if visit[nx][ny] == 0 and (nx * 5 + ny) in p:
        visit[nx][ny] = 1
        check((nx * 5 + ny))

def dfs(cnt, idx, yn):
  global ans
  global visit

  if yn >= 4 or 25 - idx < 7 - cnt:
    return

  if cnt == 7:
    check(p[0])
    if sum(sum(visit, [])) == 7:
      ans += 1
    visit = [[0] * 5 for _ in range(5)]
    return

  x = idx // 5
  y = idx % 5
  
  p.append(idx)
  if arr[x][y] == "Y":
    dfs(cnt + 1, idx + 1, yn + 1)
  else:
    dfs(cnt + 1, idx + 1, yn)
  p.pop()
  
  dfs(cnt, idx + 1, yn)

dfs(0, 0, 0)
print(ans)
#---------------------------------------------
#백트래킹만 이용한 풀이
matrix = [input() for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result_set = set()

def backtracking(arr, index, S, Y):
  if Y > 3:
    return
  if index == 7:
    arr.sort()
    result_set.add(tuple(arr))
  else:
    adjacents = []
    for node in range(len(arr)):
      for i in range(4):
        nx = arr[node][0] + dx[i]
        ny = arr[node][1] + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
          if (nx, ny) not in arr:
            adjacents.append((nx, ny))

    for adjacent in adjacents:
      nx = adjacent[0]
      ny = adjacent[1]
      if matrix[nx][ny] == "S":
        backtracking(arr + [(nx, ny)], index + 1, S + 1, Y)
      else:
        backtracking(arr + [(nx, ny)], index + 1, S, Y + 1)

for i in range(5):
  for j in range(5):
    if matrix[i][j] == "S":
      backtracking([(i, j)], 1, 1, 0)

print(len(result_set))

