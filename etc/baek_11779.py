# 2023/05/02 Baek 11779

# n 개의 도시 1 <= n <= 1000
# m 개의 버스 1 <= m <= 100,000
# A 번째 도시에서 B 번째 도시까지 가는데 드는 버스 비용 최소화
# A 번째 도시에서 B번재 도시 까지 가는데 드는 최소비용과 경로 구하기
# 항상 시작점에서 도착점으로의 경로가 존재

# 최소 비용을 구한다 -> BFS or 다익스트라
# 하지만 문제에서는 최소비용과 "경로"를 구해야함

import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[]for _ in range(n + 1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())


INF = int(1e9)

def dijkstra(start, end):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    # 비용 노드 번호
    heapq.heappush(q, (0, start, [start]))
    while q:
        dist, now, course = heapq.heappop(q)
        if now == end:
            return dist, course
        # 방문 확인 처리
        if dist > distance[now]:
            continue
        # graph는 (end, dist)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0], course + [i[0]]))

dist, course = dijkstra(start, end)
print(dist)
print(len(course))
print(* course)