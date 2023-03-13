# 2023/03/13 Baek 17390
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
A.sort()
for i in range(1, N + 1):
    A[i] += A[i - 1]

for _ in range(Q):
  L, R = map(int, input().split())
  print(A[R] - A[L - 1])