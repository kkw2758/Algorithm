# 2022/12/23 baek 12100

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def find_max_value(table):
  max_value = 0
  for i in range(len(table)):
    for j in range(len(table)):
      if max_value < table[i][j]:
        max_value = table[i][j]

  return max_value

def rotate_90(table):
  N = len(table)
  result_table = [[0] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      result_table[j][N - i - 1] = table[i][j]

  return result_table


def slide_table(table):
  result = []
  for li in table:
    li_len = len(li)
    before = 0
    idx = 0
    after = [0] * li_len
    for i in range(li_len):
      if li[i] != 0:
        if before == 0 and before != li[i]:
          before = li[i]
        elif before == li[i]:
          after[idx] = before * 2
          before = 0
          idx += 1
        elif before != li[i]:
          after[idx] = before
          before = li[i]
          idx += 1

    if before != 0:
      after[idx] = before

    result.append(after)

  return result

result = 0

def dfs(table, depth):
  global result
  if depth == 5:
    result = max(result, find_max_value(table))
    return
  for i in range(4):
    table = rotate_90(table)
    dfs(slide_table(table),depth + 1)


dfs(board, 0)
print(result)