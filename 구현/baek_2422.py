# 2023/02/21 Baek 2422

N, M = map(int, input().split())
ice = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    ice[a][b] = True
    ice[b][a] = True

result = 0

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        for k in range(j + 1, N + 1):
            if (ice[i][j] ==False and ice[i][k]== False and ice[j][k] == False):
                result += 1

print(result)