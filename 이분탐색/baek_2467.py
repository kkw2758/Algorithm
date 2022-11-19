# 2022/11/19 Baek 2467
INF = int(10e9)
N = int(input())
numbers = list(map(int, input().split()))

def parametric(first, start, end):
  before = (INF, 0, 0)
  while start <= end:
    mid = (start + end) // 2
    second = numbers[mid]
    value = first + second

    if value == 0:
      return 0, first, -first
    elif value > 0:
      end = mid - 1
    else:
      start = mid + 1

    if before[0] > abs(first + second):
      before = (abs(first + second), first, second)
    else:
      return before

  return before

result = []
for i in range(N - 1):
  first = numbers.pop(0)
  value, first, second = parametric(first, 0, len(numbers) - 1)
  result.append((value, first, second))


result.sort(key = lambda x: (x[0], -x[1]))
print(result)
print(result[0][1], result[0][2])