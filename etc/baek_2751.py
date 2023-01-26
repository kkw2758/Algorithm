# 2023/01/26 Baek 2751

N = int(input())
numbers = [False] * 1000001
for _ in range(N):
  numbers[int(input())] = True

for i in range(len(numbers)):
  if numbers[i]:
    print(i)