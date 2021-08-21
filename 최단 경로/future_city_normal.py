import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향, 소요시간 1 고정
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(1)
result1 = distance[k]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)


dijkstra(k)
result2 = distance[x]

result = result1 + result2

if result >= INF:
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