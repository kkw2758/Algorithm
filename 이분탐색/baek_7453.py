# 2022/11/23 Baek 7453

import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = []
B = []
C = []
D = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  A.append(tmp[0])
  B.append(tmp[1])
  C.append(tmp[2])
  D.append(tmp[3])

A_B = []
for i in range(N):
  for j in range(N):
    A_B.append(A[i] + B[j])

A_B_count = Counter(A_B)
ans = 0
for i in range(N):
  for j in range(N):
    target = -(C[i] + D[j])
    ans += A_B_count[target]

print(ans)


import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ab, cd = [], []
for i in range(N):
  for j in range(N):
    ab.append(arr[i][0] + arr[j][1])
    cd.append(arr[i][2] + arr[j][3])

ab.sort()
cd.sort()

i, j = 0, len(cd) - 1
result = 0

while i < len(ab) and j >= 0:
  if ab[i] + cd[j] == 0:
    nexti = i + 1
    nextj = j - 1
    while nexti < len(ab) and ab[i] == ab[nexti]:
      nexti += 1
    while nextj >= 0 and cd[j] == cd[nextj]:
      nextj -= 1
      
    result += (nexti - i) * (j - nextj)
    i = nexti
    j = nextj
  
  elif ab[i] + cd[j] > 0:
    j -= 1
  else:
    i += 1

print(result)