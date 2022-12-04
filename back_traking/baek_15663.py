# 2022/12/04 Baek 15663

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
tmp = []
visited = [False] * N
result = set()
def dfs(cnt):
  if cnt == M:
    result.add(tuple(tmp))
    return
  else:
    for i in range(N):
      if visited[i] == False:
        tmp.append(numbers[i])
        visited[i] = True
        dfs(cnt + 1)
        tmp.pop()
        visited[i] = False
        

dfs(0)
result = sorted(list(result))
for i in result:
  print(" ".join(map(str, i)))