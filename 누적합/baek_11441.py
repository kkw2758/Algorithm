# 2023/03/10 Baek 11441

import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    A[i] += A[i - 1]
M = int(input())

for _ in range(M):
    i, j = map(int, input().split())
    print(A[j] - A[i - 1])