# 2023/05/16 Baek 1158

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = [i for i in range(1, N + 1)]

idx = -1
result = []
while numbers:
    idx = (idx + K) % len(numbers)
    result.append(str(numbers.pop(idx)))
    idx -= 1

print("<" +", ".join(result) + ">")