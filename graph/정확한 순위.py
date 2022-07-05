INF = 1e9
n,m  = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# print()
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if graph[i][j] == INF:
#             print(0, end = " ")
#         else:
#             print(graph[i][j], end = " ")

#     print("")

result = 0
for i in range(1, n + 1):
    cnt = 0 
    for j in range(1, n + 1):
        if (0 < graph[i][j] < INF) or (0 < graph[j][i] < INF):
            cnt += 1
    if cnt == n - 1:
        result += 1

print(result)