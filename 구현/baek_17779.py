# 2022/11/07 baek 17779

N = int(input())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
total = 0
INF = int(1e9)
answer = INF

for i in range(1, N + 1):
    total += sum(arr[i])

def solution(x, y , d1, d2):
  temp_arr = [[0] * (N + 1) for _ in range(N + 1)]
  for i in range(d1 + 1):
    temp_arr[x + i][y - i] = 5
    temp_arr[x + d2 + i][y + d2 - i] = 59

  for i in range(d2 + 1):
    temp_arr[x + i][y + i] = 5
    temp_arr[x + d1 + i][y - d1 + i] = 5

  people = []

  
  # 구역 1
  temp = 0
  for r in range(1, x + d1):
    for c in range(1, y + 1):
      if temp_arr[r][c] == 5:
        break
      temp += arr[r][c]
  people.append(temp)

  # 구역 2
  temp = 0
  for r in range(1, x + d2 + 1):
    for c in range(N, y, -1):
      if temp_arr[r][c] == 5:
        break
      temp += arr[r][c]
  people.append(temp)

  # 구역 3
  temp = 0
  for r in range(x + d1, N + 1):
    for c in range(1, y - d1 + d2):
      if temp_arr[r][c] == 5:
        break
      temp += arr[r][c]
  people.append(temp)

  # 구역 4
  temp = 0
  for r in range(x + d2 + 1, N + 1):
    for c in range(N, y - d1 + d2 - 1, -1):
      if temp_arr[r][c] == 5:
        break
      temp += arr[r][c]
  people.append(temp)
  people.append(total - sum(people))
  return max(people) - min(people)

for x in range(1, N + 1):
  for y in range(1, N + 1):
    for d1 in range(1, N + 1):
      for d2 in range(1, N + 1):
        if (1 <= x < x + d1 + d2 <= N) and (1 <= y - d1 < y < y + d2 <= N):
          answer = min(answer, solution(x, y, d1, d2))

print(answer)