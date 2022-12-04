# 2022/12/04 Baek 15656

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
tmp = []

def dfs(cnt):
  if cnt == M:
    print(" ".join(list(map(str, tmp))))
    return
  else:
    for i in range(N):
      tmp.append(numbers[i])
      dfs(cnt + 1)
      tmp.pop()

dfs(0)