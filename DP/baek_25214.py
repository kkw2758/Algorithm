# 2022/09/25 Baek 19947

N = int(input())
ary = list(map(int, input().split()))

min_value = ary[0]
ary[0] = 0

for i in range(1, N):
  min_value = min(min_value, ary[i])
  ary[i] = max(ary[i] - min_value, ary[i - 1])

for i in ary:
  print(i, end = " ")