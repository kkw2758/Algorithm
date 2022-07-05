import heapq

n = int(input())
arr = []
INF = 1e9

for _ in range(n):
    arr.append(list(map(int, input().split())))

distance = [[INF] *(n + 1) for _ in range(n + 1)]