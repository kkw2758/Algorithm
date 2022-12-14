# # 2022/12/11 baek 14442

# import sys
# from collections import deque

# input = sys.stdin.readline
# N, M, K = map(int, input().split())
# arr = []
# for _ in range(N):
#   arr.append(list(map(int, list(input().strip()))))


# def bfs():
#   dx = [-1, 1, 0, 0]
#   dy = [0, 0, -1, 1]
#   visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
#   q = deque()
#   q.append((0, 0, K))
#   visited[0][0][K] = 1

#   while q:
#     x, y, k_cnt = q.popleft()
#     if (x, y) == (N - 1, M - 1):
#       return visited[x][y][k_cnt]
    
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if 0 <= nx < N and 0 <= ny < M:
#         # 방문 안했는데 벽이면
#         if arr[nx][ny] == 1:
#           if k_cnt > 0:
#             if visited[nx][ny][k_cnt - 1] == 0:
#               visited[nx][ny][k_cnt - 1] = visited[x][y][k_cnt] + 1
#               q.append((nx, ny, k_cnt - 1))
#         else: # 벽이 아니면
#           if visited[nx][ny][k_cnt] == 0:
#             visited[nx][ny][k_cnt] = visited[x][y][k_cnt] + 1
#             q.append((nx, ny, k_cnt))
#   return -1

# print(bfs())

import sys

input = sys.stdin.readline
num_info = [0] * 10001
for _ in range(N):
    num_info[int(input())] += 1
    
for i in range(len(num_info)):
    for j in range(num_info[i]):
        print(i)