# 2022/09/25 Baek 24417

n = int(input())


def fib(n):
  x = 0
  y = 1
  for i in range(2, n + 1):
    x, y = y % 1000000007, (x + y) % 1000000007
  return y

print(fib(n))
print(n - 2)