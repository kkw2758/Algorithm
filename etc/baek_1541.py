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