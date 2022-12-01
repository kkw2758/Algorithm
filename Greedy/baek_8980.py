# 2022/12/01 Baek 8980

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
box = [list(map(int, input().split())) for _ in range(M)]
box.sort(key = lambda x:x[1])

answer = 0
remain = [C] * (N + 1)

for i in range(M):
  temp = C
  for j in range(box[i][0], box[i][1]):
    temp = min(temp, remain[j])
  temp = min(temp, box[i][2])
  
  for j in range(box[i][0], box[i][1]):
    remain[j] -= temp
  answer += temp

print(answer)