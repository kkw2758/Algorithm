# 2022/11/28 Baek 2847

N = int(input())
numbers = []
for _ in range(N):
  numbers.append(int(input()))

cnt = 0
for i in range(N - 2, -1, - 1):
  if numbers[i + 1] <= numbers[i]:
    cnt += numbers[i] - numbers[i + 1] + 1
    numbers[i] = numbers[i + 1] - 1

print(numbers)
print(cnt)