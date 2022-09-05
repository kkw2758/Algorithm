# # 2022/09/05 Baek 1697

# # dp로 풀려고했지만 순간이동과, 그냥 이동의 가중치가 같다
# # 최소한의 시간을 구하기 위해서는 bfs 이용
from collections import deque

N, K = map(int, input().split())
distance = [0] * (100001)

def bfs(start):
  queue = deque()
  queue.append(start)

  while queue:
    now = queue.popleft()
    if now == K:
      print(distance[K])
      return distance[K]

    for next_node in (now - 1, now + 1, now * 2):
      if 0 <= next_node <= 100000 and distance[next_node] == 0:
        distance[next_node] = distance[now] + 1
        queue.append(next_node)

bfs(N)