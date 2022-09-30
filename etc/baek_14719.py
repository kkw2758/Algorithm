# 2022/09/30 Baek 14719

H, W = map(int, input().split())
ary = list(map(int, input().split()))
result = 0
for h in range(H):
  cnt = 0
  flag = False
  for w in range(W):
    if flag == False:
      if h < ary[w]:
        flag = True
    else:
      if h >= ary[w]:
        cnt += 1
      else:
        # flag = False
        result += cnt
        if cnt != 0:
          print("h = {} w = {}".format(h, w))
          print("cnt = {}".format(cnt))
        cnt = 0
    # print(flag)
print(result)
      
# 2022/09/30 Baek 14719

H, W = map(int, input().split())
ary = list(map(int, input().split()))
result = 0
for h in range(H):
  cnt = 0
  flag = False
  for w in range(W):
    if flag == False:
      if h < ary[w]:
        flag = True
    else:
      if h >= ary[w]:
        cnt += 1
      else:
        result += cnt
        cnt = 0
print(result)


from collections import deque

# 너비 우선 탐색
def bfs(x, y):
  global total
  if (1 in graph[x][y+1:]) and (1 in graph[x][:y]):
    graph[x][y] = 2
    total += 1
    q = deque()
    q.append((x, y))
  else:
    return

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # graph[0] 과 graph[-1] 에 빈 공간이 있어봐야 물이 고이지 않는다.
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        # 좌, 우를 확인해서 벽이 있다면 total += 1
        if (1 in graph[nx][ny+1:]) and (1 in graph[nx][:ny]):
          graph[nx][ny] = 2
          q.append((nx, ny))
          total += 1

# 입력
n, m = map(int,input().split())
data = list(map(int,input().split()))

# 그래프 생성
graph = [list([0] * m) for _ in range(n)]
for i in range(1, n+1):
  for j in range(m):
    if data[j] >= i:
      graph[i-1][j] = 1

total = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 전 영역을 탐색한다.
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
        bfs(i, j)
        
print(total)