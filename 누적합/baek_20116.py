# 2023/03/14 Baek 20116

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
x_list = [0] + list(map(int, input().split()))
x_copy = []

for i in range(1, n + 1):
    x_copy.append(x_list[i])
    x_list[i] += x_list[i - 1]


result = "stable"
for i in range(1, n):
    center = (x_list[-1] - x_list[i]) / (n - i)
    if not(x_copy[i - 1] - l < center < x_copy[i - 1] + l):
        result = "unstable"
        break

print(result)
