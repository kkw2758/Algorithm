# # 2022/12/10 baek 13913

# from collections import deque
# N, K = map(int, input().split())

# def bfs(start):
#   q = deque()
#   q.append([start])
#   visited = set()
#   visited.add(start)

#   while q:
#     course = q.popleft()
#     X = course[-1]
#     if X == K:
#       print(len(course) - 1)
#       for i in range(len(course)):
#         print(course[i], end = " ")
#       return

#     for i in [X + 1, X - 1, X * 2]:
#       if i not in visited:
#         visited.add(i)
#         q.append((course + [i]))

# bfs(N)


# 지나왔던 모든 경로를 큐에 저장하면서 푸니까 메모리 초과 발생
# 지나온 경로를 모두 저장한느것이 아니라 지나온 움직임을 저장
# ex) 5 > 6 > 12 > 24 > 46 경로파악
from collections import deque

def path(X):
  arr = []
  temp = X
  for _ in range(dist[X] + 1):
    arr.append(temp)
    temp = move[temp]
  print(' '.join(map(str, arr[::-1])))

def bfs():
  q = deque()
  q.append(N)

  while q:
    X = q.popleft()
    if X == K:
      print(dist[X])
      path(X)
      return

    for i in [X + 1, X - 1, X * 2]:
      if 0 <= i <= 100000 and dist[i] == 0:
        q.append(i)
        dist[i] = dist[X] + 1
        move[i] = X

N, K = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001
bfs()