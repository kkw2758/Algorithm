# 2022/12/04 Baek 15666

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
      if len(tmp) == 0:
        tmp.append(numbers[i])
        dfs(cnt + 1)
        tmp.pop()
      else:
        if tmp[-1] <= numbers[i]:
          tmp.append(numbers[i])
          dfs(cnt + 1)
          tmp.pop()          

dfs(0)
for i in sorted(result):
  print(*i)