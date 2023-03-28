# 2023/03/28 Baek 2015

import sys
from collections import defaultdict
input = sys.stdin.readline
int_dict = defaultdict(int)

N, K = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
result = 0
int_dict[0] = 1
for i in range(1, N + 1):
    numbers[i] += numbers[i - 1]
    result += int_dict[numbers[i] - K]
    int_dict[numbers[i]] += 1

print(result)
