# 2022/12/01 Baek 7570

import sys
input = sys.stdin.readline

lines = []
N = int(input())
for _ in range(N):
  lines.append(list(map(int, input().split())))

lines.sort()
start = lines[0][0]
end = lines[0][1]

result = 0
for i in range(1, N):
  if end >= lines[i][0]:
    if end < lines[i][1]:
      end = lines[i][1]
  else:
    result += end - start
    start = lines[i][0]
    end = lines[i][1]

result += end - start
print(result)