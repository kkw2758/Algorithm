# 2022/11/17 baek_10816

from bisect import bisect_left, bisect_right

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
targets = list(map(int, input().split()))

for i in range(M):
    print(bisect_right(arr, targets[i]) - bisect_left(arr, targets[i]), end = " ")