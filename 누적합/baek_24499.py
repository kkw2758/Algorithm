# 2023/03/21 Baek 24499

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [0] + list(map(int, input().split())) * 2

for i in range(1, 2 * N + 1):
    A[i] += A[i - 1]
result = 0
for i in range(K, 2 * N + 1):
    result = max(result, A[i] - A[i - K])
print(result)