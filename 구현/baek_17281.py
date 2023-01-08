# # 2022/12/26 baek 17281

# import sys
# from itertools import permutations

# input = sys.stdin.readline

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# max_score = 0
# candidates = permutations(list(range(1,9)), 8)

# for candidate in candidates:
#   # 1번 타자가 4번째 타순
#   candidate = list(candidate)
#   candidate.insert(3, 0)
#   score = 0
#   idx = 0
#   for i in range(N):
#     status = [False, False, False]
#     out_cnt = 0
#     while out_cnt < 3:
#       if board[i][candidate[idx]] == 1:
#         for _ in range(board[i][candidate[idx]]):
#           if status.pop() == True:
#             score += 1
#         status = [True] + status
#         idx = (idx + 1) % 9

#       elif board[i][candidate[idx]] == 2:
#         for _ in range(board[i][candidate[idx]]):
#           if status.pop() == True:
#             score += 1
#         status = [False, True] + status
#         idx = (idx + 1) % 9

#       elif board[i][candidate[idx]] == 3:
#         for _ in range(board[i][candidate[idx]]):
#           if status.pop() == True:
#             score += 1
#         status = [False, False, True] + status
#         idx = (idx + 1) % 9

#       elif board[i][candidate[idx]] == 4:
#         score += 1
#         for _ in range(board[i][candidate[idx]] - 1):
#           if status.pop() == True:
#             score += 1
#         status = [False, False, False] + status
#         idx = (idx + 1) % 9

#       else:
#         idx = (idx + 1) % 9
#         out_cnt += 1

#   max_score = max(max_score, score)

# print(max_score)


# # 시간 초과 해결 - 순열
# import sys
# from itertools import permutations

# input = sys.stdin.readline

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# max_score = 0
# candidates = permutations(list(range(1,9)), 8)

# for candidate in candidates:
#   candidate = list(candidate)
#   candidate.insert(3, 0)
#   score = 0
#   idx = 0
#   for i in range(N):
#     out_cnt = 0
#     b1, b2, b3 = 0, 0, 0
#     inning = board[i]
#     while out_cnt < 3:
#       if inning[candidate[idx]] == 0:
#         out_cnt += 1
#       elif inning[candidate[idx]] == 1:
#         score += b3
#         b1, b2, b3 = 1, b1, b2
#       elif inning[candidate[idx]] == 2:
#         score += (b2 + b3)
#         b1, b2, b3 = 0, 1, b1
#       elif inning[candidate[idx]] == 3:
#         score += (b1 + b2 + b3)
#         b1, b2, b3 = 0, 0, 1
#       elif inning[candidate[idx]] == 4:
#         score += (1 + b1 + b2 + b3)
#         b1, b2, b3 = 0, 0, 0

#       idx = (idx + 1) % 9
#   max_score = max(max_score, score)

# print(max_score)

# 시간 초과 해결 - 백트래킹

import sys

input = sys.stdin.readline

def dfs(cnt):
  global ans
  if cnt == 9:
      start, score = 0, 0
      for inning in a:
          out, b1, b2, b3 = 0, 0, 0, 0
          while out <= 2:
              p = select[start]
              if inning[p] == 0:
                  out += 1
              elif inning[p] == 1:
                  score += b3
                  b1, b2, b3 = 1, b1, b2
              elif inning[p] == 2:
                  score += b2 + b3
                  b1, b2, b3 = 0, 1, b1
              elif inning[p] == 3:
                  score += b1 + b2 + b3
                  b1, b2, b3 = 0, 0, 1
              else:
                  score += b1 + b2 + b3 + 1
                  b1, b2, b3 = 0, 0, 0

              start += 1
              start %= 9

      ans = max(ans, score)
      return

  for i in range(9):
    if c[i]:
        continue
    c[i] = 1
    select[i] = cnt
    dfs(cnt + 1)
    c[i] = 0
    select[i] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
select, c = [0 for _ in range(9)], [0 for _ in range(9)]
select[3], c[3] = 0, 1
ans = 0
dfs(1)
print(ans)