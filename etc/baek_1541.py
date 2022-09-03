# 2022/09/03 Baek 1541

problem = input().split("-")

result = 0
for i in range(len(problem)):
  if i == 0:
    b = problem[i].split("+")
    b = list(map(int, b))
    result += sum(b)
    continue
  b = problem[i].split("+")
  b = list(map(int, b))
  result -= sum(b)

print(result)

def solve(arr):
  sorted_arr = sorted(arr)
  d = {x: idx for idx, x in enumerate(sorted_arr)}
  return [d[x] for x in arr]
N = input()