# 2022/12/04 Baek 15664

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

tmp = []
result = set()
def dfs(cnt, idx):
  if cnt == M:
    result.add(tuple(tmp))
  else:
    for i in range(idx, N):
      tmp.append(numbers[i])
      dfs(cnt + 1, i + 1)
      tmp.pop()

dfs(0,0)

for i in sorted(result):
  print(*i)