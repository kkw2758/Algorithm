# 2023/03/13 Baek 12847

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
T = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    T[i] += T[i - 1]

result = 0

for i in range(m, n):
    result = max(result, T[i] - T[i-m])

print(result)