# import sys

# input = sys.stdin.readline
# N, L, R = map(int, input().split())

# graph = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# visited = [[False] * N for _ in range(N)]
# for _ in range(N):
#     graph.append(list(map(int, input().split())))

 
# def dfs(x, y):
#     stack = []
#     stack.append((x,y))
#     visited[x][y] = True
#     total_before_value = 0
#     target_list = []
#     while stack:
#         x, y = stack.pop()
#         total_before_value += graph[x][y]
#         target_list.append((x,y))
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if L <= abs(graph[x][y] - graph[nx][ny]) <= R and not visited[nx][ny]:
#                     visited[nx][ny] = True
#                     stack.append((nx,ny))
                    

#     if len(target_list) > 1:
#         after_value = total_before_value // len(target_list)
#         for x, y in target_list:
#             graph[x][y] = after_value
#         return True
    
#     return False


# for cnt in range(2000):
#     visited = [[False] * N for _ in range(N)]
#     flag = False
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 result = dfs(i,j)
#                 if result:
#                     flag = True

#     if not flag:
#         break

# print(cnt)

# # 이것이 취업을 위한 코딩 테스트다 with 파이썬 해설 참고
# # BFS
# from collections import deque

# n, l, r = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# result = 0

# def process_bfs(x, y, index):
#     united = []
#     united.append((x, y))

#     q = deque()
#     q.append((x,y))
#     union[x][y] = index
#     summary = graph[x][y]
#     count = 1
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
#                 if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
#                     q.append((nx, ny))
#                     union[nx][ny] = index
#                     summary += graph[nx][ny]
#                     count += 1
#                     united.append((nx,ny))

#     for i, j in united:
#         graph[i][j] = summary // count
    
#     return count

# total_count = 0

# while True:
#     union = [[-1] * n for _ in range(n)]
#     index = 0
#     for i in range(n):
#         for j in range(n):
#             if union[i][j] == -1:
#                 process_bfs(i, j, index)
#                 index += 1
    
#     if index == n * n:
#         break
#     total_count += 1

# print(total_count)


# #DFS
# from collections import deque

# n, l, r = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# result = 0

# def process_dfs(x, y, index):
#     united = []
#     united.append((x, y))
#     stack = [(x, y)]
#     union[x][y] = index
#     summary = graph[x][y]
#     count = 1
#     while stack:
#         x, y = stack.pop()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
#                 if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
#                     stack.append((nx, ny))
#                     union[nx][ny] = index
#                     summary += graph[nx][ny]
#                     count += 1
#                     united.append((nx,ny))

#     for i, j in united:
#         graph[i][j] = summary // count
    
#     return count

# total_count = 0

# while True:
#     union = [[-1] * n for _ in range(n)]
#     index = 0
#     for i in range(n):
#         for j in range(n):
#             if union[i][j] == -1:
#                 process_dfs(i, j, index)
#                 index += 1
    
#     if index == n * n:
#         break
#     total_count += 1

# print(total_count)


# # 백준 python 최고속도 풀이
# # 격자 모양으로 탐색하면서 탐색 횟수 최소화

# from collections import deque
# import sys
# input = sys.stdin.readline

# def main():
#     n, l, r = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[-1] * n for _ in range(n)]
#     cnt = 0
#     move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
#     cand = deque([(i, j) for i in range(n) for j in range(i % 2, n, 2)])

#     while True:
#         q = deque()
#         for _ in range(len(cand)):
#             i, j = cand.popleft()
#             if visited[i][j] == cnt:
#                 continue
#             visited[i][j] = cnt
#             area = set([(i, j)])
#             popul = board[i][j]
#             q.append((i, j))

#             # BFS
#             while q:
#                 x, y = q.popleft()
#                 for a, b in move:
#                     dx = x + a
#                     dy = y + b
#                     if dx >= n or dx < 0 or dy >= n or dy < 0 or visited[dx][dy] == cnt:
#                         continue

#                     if l <= abs(board[x][y] - board[dx][dy]) <= r:
#                         visited[dx][dy] = cnt
#                         area.add((dx, dy))
#                         popul += board[dx][dy]
#                         q.append((dx, dy))

#             if len(area) > 1:
#                 avg_popul = popul // len(area)
#                 for x, y in area:
#                     board[x][y] = avg_popul
#                     cand.append((x, y))

#         if cand:
#             cnt += 1
#         else:
#             break
#     print(cnt)
# main()

import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
A = []

for _ in range(n):
    A.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(start_x, start_y):
    members = [(start_x, start_y)]
    stack = [(start_x, start_y)]
    visited[start_x][start_y] = True
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and l <= abs(A[x][y] - A[nx][ny]) <= r and not(visited[nx][ny]):
                members.append((nx, ny))
                visited[nx][ny] = True
                stack.append((nx, ny))

    return members

cnt = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for row in range(n):
        for col in range(n):
            if not(visited[row][col]):
                members = dfs(row, col)
                if len(members) != 1:
                    flag = True
                    total_population = 0
                    for member in members:
                        total_population += A[member[0]][member[1]]

                    after_population = int(total_population / len(members))
                    for member in members:
                        A[member[0]][member[1]] = after_population
    if not(flag):
        break
    else:
        cnt += 1


print(cnt)