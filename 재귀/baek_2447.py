# 2023/03/03 Baek 2447

N = int(input())

def recursive(N):
  if N == 1:
    return "*"
  
  stars = []
  pattern = recursive(N//3)
  for p in pattern:
    stars.append(p*3)
  for p in pattern:
    stars.append(p + " " * (N//3) + p)
  for p in pattern:
    stars.append(p*3)

  return stars

print("\n".join(recursive(N)))



def recursive(N):
    if N == 3:
        g[1][:3] = ["*", " ", "*"]
        g[0][:3] = g[2][:3] = ["*"] * 3
        return
    
    recursive(N//3)
    
    for i in range(0, N, N//3):
        for j in range(0, N, N//3):
            if i != N//3 or j != N//3:
                for k in range(N//3):
                    g[i + k][j:j+N//3] = g[k][:N//3]


N = int(input())

g = [[" " for _ in range(N)] for _ in range(N)]
recursive(N)

for i in range(N):
    for j in range(N):
        print(g[i][j], end='')
    print()