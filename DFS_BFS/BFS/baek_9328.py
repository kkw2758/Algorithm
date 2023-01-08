# # 2022/12/29 Baek 9328

# # 내가 짠 코드 시간 초과
# import sys
# from collections import deque

# input = sys.stdin.readline

# def bfs(start, keys):
#   flag = False
#   result = 0
#   q = deque()
#   visited = [[False] * w for _ in range(h)]

#   dx = [-1, 1, 0, 0]
#   dy = [0, 0, -1, 1]

#   for x, y in start:
#     q.append((x, y))
#     visited[x][y] = True

#   while q:
#     x, y = q.popleft()
#     if (x, y) in visited:
#       continue
#     if board[x][y] == ".":
#       visited.append((x, y))

#     if board[x][y] == "$":
#       result += 1
#       visited.append((x, y))

#     if board[x][y].isupper():
#       if board[x][y].lower() in keys:
#         board[x][y] = "."
#         visited.append((x, y))
#       else:
#         continue
#     if board[x][y].islower():
#       if board[x][y] not in keys:
#         flag = True
#         keys += board[x][y]
#         board[x][y] = "."
#         visited.append((x, y))

#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
      
#       if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
#         if board[nx][ny] != "*":
#           q.append((nx, ny))

#   return flag, result, keys

# t = int(input())
# for _ in range(t):
#   h, w = map(int, input().split())
#   board = [list(input().rstrip()) for _ in range(h)]
#   keys = input()
#   start = []

#   for i in range(h):
#     for j in range(w):
#       if i == 0 or j == 0 or i == (h - 1) or j == (w - 1):
#         if board[i][j] != "*":
#           start.append((i, j))

#   while True:
#     flag, result, keys = bfs(start, keys)
#     if flag == False:
#       break

#   print(result)

# # 코드 참조 1
# from collections import deque
# import sys
# input = sys.stdin.readline

# t = int(input())

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs():
#   de = deque()
#   de.append([0, 0])
#   ch[0][0] = 0
#   dq = [deque() for i in range(26)]
#   r = 0

#   while de:
#     x, y = de.popleft()
#     for i in range(4):
      
#       nx = x + dx[i]
#       ny = y + dy[i]
      
#       if 0 <= nx < h + 2 and 0 <= ny < w + 2:
        
#         if a[nx][ny] == "*":
#           continue

#         if ch[nx][ny] == -1:
#           ch[nx][ny] = 0

#           if a[nx][ny] == "$":
#             r += 1
#           elif a[nx][ny].isupper():
#             d = ord(a[nx][ny]) - ord("A")
#             if alp[d] == False:
#               dq[d].append([nx, ny])
#               continue
#           elif a[nx][ny].islower():
#             k = ord(a[nx][ny]) - ord('a')
#             alp[k] = True
#             while dq[k]:
#               kx, ky = dq[k].popleft()
#               de.append([kx, ky])

#           de.append([nx, ny])

#   return r

# for _ in range(t):
#   h, w = map(int, input().split())

#   a = [list('.' * (w + 2))]
#   for i in range(h):
#     a.append(list("." + input().rstrip() + "."))
#   a.append(list("." * (w + 2)))
#   k = input().rstrip()

#   ch = [[-1] * (w + 2) for i in range(h + 2)]
#   alp = [False] * 26
#   if k != "0":
#     for i in k:
#       alp[ord(i) - ord('a')] = True

#   print(bfs())

# 참조 코드 2
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  q = deque()
  c = [[0] * (w + 2) for _ in range(h + 2)]
  q.append([x, y])
  c[x][y] = 1
  cnt = 0
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < h + 2 and 0 <= ny < w + 2:
        if not c[nx][ny]:
          if a[nx][ny] == ".":
            c[nx][ny] = 1
            q.append([nx, ny])
          elif a[nx][ny].islower():
            door[ord(a[nx][ny]) - ord('a')] = 1
            q = deque()
            c = [[0] * (w + 2) for _ in range(h + 2)]
            a[nx][ny] = '.'
            q.append([nx, ny])
          elif a[nx][ny].isupper():
            if door[ord(a[nx][ny]) - ord("A")]:
              c[nx][ny] == 1
              a[nx][ny] = "."
              q.append([nx, ny])
          elif a[nx][ny] == "$":
            c[nx][ny] = 1
            cnt += 1
            a[nx][ny] = "."
            q.append([nx, ny])
  print(cnt)

def new_map():
  for i in a:
    i.insert(0, ".")
    i.append(".")
  a.insert(0, ['.'] * (w + 2))
  a.append(['.'] * (w + 2))

tc = int(input())
while tc:
  h, w = map(int, input().split())
  a = [list(input().strip()) for _ in range(h)]
  key = list(input().strip())
  door = [0] * 26

  for k in key:
    if k != "0":
      door[ord(k) - ord('a')] = 1

  for i in range(h):
    for j in range(w):
      if a[i][j].isupper():
        if door[ord(a[i][j]) - ord('A')]:
          a[i][j] = "."
  new_map()
  bfs(0, 0)
  tc -= 1