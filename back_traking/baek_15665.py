# 2022/12/04 Baek 15665

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

tmp = []
result = set()
def dfs(cnt):
  if cnt == M:
    result.add(tuple(tmp))
  else:
    for i in range(N):
      tmp.append(numbers[i])
      dfs(cnt + 1)
      tmp.pop()

dfs(0)

for i in sorted(result):
  print(*i)