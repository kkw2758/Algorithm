# 2022/12/04 Baek 6603

def dfs(cnt, idx):
  if cnt == 6:
    print(" ".join(map(str, tmp)))
  else:
    for i in range(idx, K):
      tmp.append(S[i])
      dfs(cnt + 1, i + 1)
      tmp.pop()

while True:
  k = list(map(int, input().split()))
  if k[0] == 0:
    break
  K = k[0]
  S = k[1:]
  tmp = []
  dfs(0, 0)
  print()