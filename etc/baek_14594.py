# 2022/12/18 Baek 14594

N = int(input())
M = int(input())

wall_info = [True] * N

for _ in range(M):
  x, y = map(int, input().split())
  for i in range(x, y):
    if wall_info[i]:
      wall_info[i] = False

cnt = 1
for i in range(1, N):
  if wall_info[i]:
    cnt += 1

print(cnt)