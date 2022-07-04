# 2022/03/10 Baek 18310

import sys

input = sys.stdin.readline
n = int(input())
house_list = list(map(int, input().split()))
house_list.sort()
print(house_list[(n - 1) // 2])