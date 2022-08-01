def rotate_90(matrix):
  n = len(matrix)
  ret = [[0] * n for _ in range(n)]
  for row in range(n):
    for col in range(n):
      new_row = col
      new_col = n - 1 - row
      ret[new_row][new_col] = matrix[row][col]

  return ret

def check(new_lock):
  lock_length = len(new_lock) // 3
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1:
        return False
  return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
      for j in range(n):
        new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
      key = rotate_90(key)
      for x in range(n * 2):
        for y in range(n * 2):
          
          for i in range(m):
            for j in range(m):
              new_lock[x + i][y + j] += key[i][j]

          if check(new_lock) == True:
            return True

          for i in range(m):
            for j in range(m):
              new_lock[x + i][y + j] -= key[i][j]
    return False