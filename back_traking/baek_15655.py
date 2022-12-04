# 2022/12/04 Baek 15655

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
tmp = []
def dfs(cnt):
  if cnt == M:
    print(' '.join(map(str, tmp)))
    return
  for i in range(N):
    if len(tmp) == 0:
      tmp.append(lst[i])
      dfs(cnt + 1)
      tmp.pop()
    else:
      if tmp[-1] < lst[i]:
        tmp.append(lst[i])
        dfs(cnt + 1)
        tmp.pop()
dfs(0)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = []
visited = [False] * N

def dfs(cnt, start):
  if cnt == M:
    print(' '.join(map(str, result)))
    return
  for i in range(start, N):
    if visited[i]:
      continue
    
    visited[i] = True
    result.append(lst[i])

    dfs(cnt + 1, i + 1)

    result.pop()
    visited[i] = False

dfs(0, 0)