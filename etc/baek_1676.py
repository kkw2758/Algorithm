# 2022/09/01 Baek 1676

def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

n = int(input())
fact = factorial(n)
cnt = 0
while True:
  if fact % 10 != 0:
    break
  fact = fact // 10
  cnt += 1

print(cnt)