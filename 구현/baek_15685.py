#2022/11/01 baek 15685
import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * 101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
  x, y, d, g = map(int, input().split())
  arr[x][y] = 1
  dragon = [d]
  for i in range(g):
    temp = []
    for j in range(len(dragon) - 1, -1, -1):
      temp.append((dragon[j] + 1) % 4)
    dragon += temp

  for i in range(len(dragon)):
    nx = x + dx[dragon[i]]
    ny = y + dy[dragon[i]]
    arr[nx][ny] = 1
    x = nx
    y = ny

ans = 0
for i in range(100):
  for j in range(100):
    if arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1]:
      ans += 1

print(ans)