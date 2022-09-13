# 2022/09/12 Baek 14500

# 원래 나의 풀이
# 아이디어는 맞아 떨어졌지만 시간초과 발생
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# graph = []

# for _ in range(N):
#   graph.append(list(map(int, input().split())))

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# result = 0

# def dfs(x, y, cnt, visited):
#   global result
#   if cnt == 4:
#     temp = 0
#     for i, j in visited:
#       temp += graph[i][j]
#     result = max(result, temp)
#     return
#   for idx in range(4):
#     nx = x + dx[idx]
#     ny = y + dy[idx]
#     if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
#       dfs(nx, ny, cnt + 1, visited + [(nx, ny)])

# def check(x, y):
#   global result
#   block_cnt = 0
#   total = graph[x][y]
#   for idx in range(4):
#     nx = x + dx[idx]
#     ny = y + dy[idx]
#     if 0 <= nx < N  and 0 <= ny < M:
#       block_cnt += 1
#       total += graph[nx][ny]

#   if block_cnt == 3:
#     if result < total:
#       result = total
#   elif block_cnt == 4:
#     for i in range(4):
#       nx = x + dx[idx]
#       ny = y + dy[idx]
#       total -= graph[nx][ny]
#       if total > result:
#         result = total
#       total += graph[nx][ny]

  
# for i in range(N):
#   for j in range(M):
#     dfs(i, j, 0, [])
#     check(i, j)

# print(result)

import sys

input = sys.stdin.readline

def dfs(x, y, cnt, total):
  global ans
  if cnt == 3:
    if total > ans:
      ans = total
  else:
    for idx in range(4):
      nx = x + dx[idx]
      ny = y + dy[idx]
      if 0 <= nx < N and 0 <= ny < M:
        if not visited[nx][ny]:
          visited[nx][ny] = True
          dfs(nx, ny, cnt + 1, total + graph[nx][ny])
          visited[nx][ny] = False

def block(x, y, total):
  global ans
  block_cnt = 0
  for idx in range(4):
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0 <= nx < N and 0 <= ny < M:
      block_cnt += 1
      total += graph[nx][ny]

  if block_cnt == 3:
    if total > ans:
      ans = total
  
  if block_cnt == 4:
    for idx in range(4):
      nx = x + dx[idx]
      ny = y + dy[idx]
      total -= graph[nx][ny]
      if total > ans:
        ans = total
      total += graph[nx][ny]

N, M = map(int, input().split())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
ans = 0

for i in range(N):
  for j in range(M):
    visited[i][j] = True
    dfs(i, j, 0, graph[i][j])
    block(i, j, graph[i][j])
    visited[i][j] = False

print(ans)




# 가지치기 적용한 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, graph))

def dfs(x, y, cnt, total):
  global ans
  if ans >= total + max_val * (3 - cnt):
    return
  if cnt == 3:
    ans = max(ans, total)
    return
  else:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and  visited[nx][ny] == False:
        if cnt == 1:
          visited[nx][ny] = 1
          dfs(x, y, cnt + 1, total + graph[nx][ny])
          visited[nx][ny] = 0

        visited[nx][ny] = 1
        dfs(nx, ny, cnt + 1, total + graph[nx][ny])
        visited[nx][ny] = 0

for i in range(N):
  for j in range(M):
    visited[i][j] = 1
    dfs(i, j, 0, graph[i][j])
    visited[i][j] = 0

print(ans)