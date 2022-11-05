# 2022/11/05 baek 14890
import sys
input = sys.stdin.readline

# 한 행, 열 받음
def check(arr):
  visited = [False] * N
  for i in range(1, N):
    if abs(arr[i] - arr[i - 1]) > 1:
      return False

    if arr[i] > arr[i - 1]:
      for j in range(i - 1, i - 1 - L, -1):
        if j < 0 or arr[i - 1] != arr[j] or visited[j]:
          return False
        visited[j] = True

    elif arr[i] < arr[i - 1]:
      for j in range(i, i + L):
        if  j >= N or arr[i] != arr[j] or visited[j]:
          return False
        visited[j] = True

  return True

N, L = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))

cnt = 0
for i in range(N):
  if check(arr[i]):
    cnt += 1

for i in range(N):
  temp = []
  for j in range(N):
    temp.append(arr[j][i])
  if check(temp):
    cnt += 1

print(cnt)