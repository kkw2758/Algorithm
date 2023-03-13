# 2023/03/10 Baek 10025

import sys

input = sys.stdin.readline
cage = [0 for _ in range(1000001)]

N, K = map(int, input().split())
for _ in range(N):
    g, x = map(int, input().split())
    cage[x] = g

for i in range(1, 1000001):
    cage[i] += cage[i-1]


result = 0
if K * 2 + 1 > 1000000:
    print(cage[-1])
else:
    for i in range(K*2 + 1, 1000001):
        if i - (K * 2 + 1) >= 0:
            idx = i - (K * 2 + 1)
        else:
            idx = 0
        result = max(result, cage[i] - cage[idx])
    print(result)


# import sys

# input = sys.stdin.readline
# n, k = map(int, sys.stdin.readline)

# ice = [0] * 1