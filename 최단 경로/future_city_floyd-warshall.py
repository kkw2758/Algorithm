INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if row == col:
            graph[row][col] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][k] + graph[k][x]

if result > INF:
    print(-1)
else:
    print(result)

'''
ex1)
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

ex2)
4 2
1 3
2 4
3 4
'''