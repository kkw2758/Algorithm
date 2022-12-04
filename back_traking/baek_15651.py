# 2022/12/02 Baek 15651

N, M = map(int, input().split())

def back_tracking(cnt, numbers):
  if cnt == M:
    for number in numbers:
      print(number, end = " ")
    print()
    return
  else:
    for i in range(1, N + 1):
      back_tracking(cnt + 1, numbers + [i])

back_tracking(0, [])

N, M = map(int, input().split())
lst = []

def dfs(cnt):
  if cnt == M:
    print(' '.join(map(str, lst)))
    return
  for i in range(1, N + 1):
    lst.append(i)
    dfs(cnt + 1)
    lst.pop()
dfs(0)