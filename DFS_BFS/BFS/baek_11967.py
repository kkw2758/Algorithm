# 2022/12/18 Baek 11967

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
turninfo = defaultdict(list)


for _ in range(M):
  x, y, a, b = map(int, input().split())
  turninfo[(x, y)].append((a, b))

def bfs():
  result = 1
  room_info = [[False] * (N + 1) for _ in range(N + 1)]
  visited = [[-1] * (N + 1) for _ in range(N + 1)]
  room_info[1][1] = True

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  q = deque()
  q.append((1, 1))
  visited[1][1] = 1
  while q:
    x, y = q.popleft()
    # 불켜주기
    for s_x, s_y in turninfo[(x, y)]:
      if not room_info[s_x][s_y]:
          room_info[s_x][s_y] = True
          result += 1
          # 불킨곳 주변에 방문한 곳이 있다면 재방문의 가능성이 있으므로 큐에 추가
          for i in range(4):
            nx = s_x + dx[i]
            ny = s_y + dy[i]
            if 1 <= nx < (N + 1) and 1 <= ny < (N + 1):
              if visited[nx][ny] == 1:
                q.append((nx, ny))

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # nx, ny 가 범위가 맞고 아직 방문하지 않았으며 불이 켜져있으면 > 방문
      if 1 <= nx < (N + 1) and 1 <= ny < (N + 1) and room_info[nx][ny] and visited[nx][ny] == -1:
        visited[nx][ny] = 1
        q.append((nx, ny))
  return result

print(bfs())

'''
4 10
1 1 1 2
1 2 1 3
1 2 4 1
1 3 1 4
1 3 3 1
1 4 2 4
1 4 2 1
2 1 4 4
3 1 4 3
4 1 3 4
'''