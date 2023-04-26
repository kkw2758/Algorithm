# 2023/04/26 Baek 1238

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# N개로 숫자로 구분된 각각의 마을
# M개의 단방향 도로
# X 번 마을 갔다가 다시 돌아와야함

N, M, X = map(int, input().split())

# 연결 그래프
graph = [[] for _ in range(N + 1)]
for i in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dijkstra(start):
    # 시작점 설정
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        # 방문체크를 해야함
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 거리
distance = [INF] * (N + 1)
dijkstra(X)
return_dist = distance[:]

result = 0
for i in range(1, N + 1):
    distance = [INF] * (N + 1)
    dijkstra(i)
    result = max(result, return_dist[i] + distance[X])

print(result)