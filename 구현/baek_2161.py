# 2023/02/17 Baek 2161

N = int(input())
numbers = [i for i in range(1, N + 1)]
for i in range(N):
    print(numbers.pop(0), end = " ")
    if len(numbers) == 1:
      print(numbers[0], end= "")
      break
    numbers.append(numbers.pop(0))
