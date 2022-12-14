import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(list(map(int, list(input().rstrip()))))

visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]

def bfs():
  q = []
  heapq.heappush(q, (1, 0, 0, 0))
  visited[0][0][0] = True
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  #홀수 낮, 짝수 밤
  #낮에만 부실수 있음

  while q:
    dist, k, x, y = heapq.heappop(q)
    if (x, y) == (N - 1, M - 1):
      return dist
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        # 다음이 벽이고 깰 수 있으면
        if arr[nx][ny] == 1 and k < K:
          if visited[nx][ny][k + 1] == False:
            #짝수 밤, 홀수 낮
            if dist % 2 == 1:
              # print("wall morning", nx, ny, k)
              visited[nx][ny][k + 1] = True
              heapq.heappush(q, (dist + 1, k + 1, nx, ny))
            elif dist % 2 == 0:
              # print("wall evening", nx, ny, k)
              visited[nx][ny][k + 1] = True
              heapq.heappush(q, (dist + 2, k + 1, nx, ny))
        # 벽이아니면
        elif arr[nx][ny] == 0:
          if visited[nx][ny][k] == False:
            # print("not wall", nx, ny, k)
            visited[nx][ny][k] = True
            heapq.heappush(q, (dist + 1, k, nx, ny))
    
  return -1

print(bfs())