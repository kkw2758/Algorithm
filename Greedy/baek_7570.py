# 2022/12/01 Baek 7570

N = int(input())
numbers = list(map(int, input().split()))

temp = [0] * (N + 1)

for i in numbers:
  temp[i] = temp[i - 1] + 1

print(N - max(temp))