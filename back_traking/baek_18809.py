# 2022/12/05 Baek 18809

N, M, R, G = map(int, input().split())
garden = []
for _ in range(N):
  garden.append(list(map(int, input().split())))

result = 0
R_territory = []
G_territory = []

def bfs():
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

def dfs(R_cnt, G_cnt, start):
  if R_cnt > R or G_cnt > G:
    return
  if R_cnt == R and G_cnt == G:
    print("R", R_territory)
    print("G", G_territory)
    return

  for i in range(start, N * M):
    x = i // M
    y = i % M
    if garden[x][y] == 2:
      if (x, y) in R_territory or (x, y) in G_territory:
        continue
      else:
        G_territory.append((x, y))
        dfs(R_cnt, G_cnt + 1, i + 1)
        G_territory.pop()

        R_territory.append((x, y))
        dfs(R_cnt + 1, G_cnt, i + 1)
        R_territory.pop()

dfs(0, 0, 0)