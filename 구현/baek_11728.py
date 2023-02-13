# 2023/02/07 Baek 11728

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
result = sorted(A+B)
for i in result:
  print(i, end = " ")