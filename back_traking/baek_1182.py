# 2022/12/04 Baek 1182

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0
tmp = []

def dfs(idx):
  global result
  if idx >= N:
    return
  else:
    for i in range(idx, N):
      tmp.append(numbers[i])
      if sum(tmp) == S:
        result += 1
      dfs(i + 1)
      tmp.pop()

dfs(0)
print(result)

# 다른 풀이
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0

def dfs(num, sum):
  global cnt
  if num >= N:
    return
  sum += numbers[num]
  if sum == S:
    cnt += 1

  dfs(num + 1, sum)
  dfs(num + 1, sum - numbers[num])
  
dfs(0, 0)
print(cnt)