# 2022/11/11 Baek 20609

N, M = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
arr = [list(map(int, input().split())) for _ in range(N)]
rainbow_blocks = []

# for i in range(N):
#   for j in range(N):
#     if arr[i][j] == 0:
#       rainbow_blocks.append((i, j))

def rotate_90(arr):
  n = len(arr)
  temp = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      temp[n - 1 - j][i] = arr[i][j]

  return temp

#빈곳이라면 -2
def gravity(arr):
  for i in range(N - 1, -1, -1):
    for j in range(N):
      # 검은 블록이 아니라면 중력의 영향을 받음
      if arr[i][j] != -1 and arr[i][j] != -2:
        index = i
        for k in range(i + 1, N):
          if arr[k][j] == -2:
            index = k
          else:
            index = k - 1
            break
        if index != i:
          arr[index][j] = arr[i][j]
          arr[i][j] = -2
  return arr
# 블록 크기, 무지개 포함수, 행, 열, 멤버 좌표

def solution(arr):
  result = 0
  while True:
    visited = [[False] * N for _ in range(N)]
    block_groups = []
    for i in range(N):
      for j in range(N):
        blocks = []
        if arr[i][j] > 0 and visited[i][j] == False:
          block_color = arr[i][j]
          rainbow_blocks = []
          stack = []
          stack.append((i, j))

          while stack:
            x, y = stack.pop()
            for k in range(4):
              nx = x + dx[k]
              ny = y + dy[k]
              if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if arr[nx][ny] == block_color:
                  visited[nx][ny] = True
                  blocks.append((nx, ny))
                  stack.append((nx, ny))

                elif arr[nx][ny] == 0:
                  visited[nx][ny] = True
                  blocks.append((nx, ny))
                  stack.append((nx, ny))
                  rainbow_blocks.append((nx, ny))

          if len(blocks) >= 2:
            not_rainbow_blocks = list(set(blocks) - set(rainbow_blocks))
            not_rainbow_blocks.sort()
            block_groups.append((len(blocks), len(rainbow_blocks), not_rainbow_blocks[0][0], not_rainbow_blocks[0][1], blocks))
          
          for x, y in rainbow_blocks:
            visited[x][y] = False

    if len(block_groups) == 0:
      return result
 
    block_groups.sort(reverse=True)
    cnt = len(block_groups[0][4])
    result += cnt ** 2
    for x, y in block_groups[0][4]:
      arr[x][y] = -2
      
    arr = gravity(arr)
    arr = rotate_90(arr)
    arr = gravity(arr)

print(solution(arr))