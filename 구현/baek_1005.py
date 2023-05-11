# 2023/05/11 Baek 1005

import sys
input = sys.stdin.readline

# 나의 풀이 - 완전 탐색
def solution():
  N, K = map(int, input().split())
  times = list(map(int, input().split()))
  total_time = 0

  # N 건물의 수
  buildings = [[] for _ in range(N + 1)]
  for i in range(K):
    X, Y = map(int, input().split())
    buildings[Y].append(X)

  W = int(input())

  visited_buildings = []
  while True:
    can_build_buildings = []
    for i in range(1, N + 1):
      # 현재 방문하고자 하는 건물이전에 지어야 하는 건물이 전부다 지어졌으면
      if i not in visited_buildings:
        build_flag = True
        for building in buildings[i]:
          if building not in visited_buildings:
            build_flag = False

        if build_flag:
          can_build_buildings.append(i)

    if W in can_build_buildings:
      total_time += times[W - 1]
      return total_time
    
    time = 0
    # 방문처리
    for can_build_building in can_build_buildings:
      time = max(time, times[can_build_building - 1])
      visited_buildings.append(can_build_building)
    total_time += time
  
T = int(input())
for _ in range(T):
  print(solution())


# 큐를 이용한 위상정렬 알고리즘
# 1. 진입차수가 0인 모든 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
#   1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
#   2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
# 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과가 도니다.

from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)  # 정점 A에서 B로 이동 가능
  # 진입 차수를 1 증가
  indegree[b] += 1

# 우시ㅏㅇ 정렬 함수
def topology_sort():
  result = [] # 알고리즘 수행 결과를 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용
  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
  # 큐가 빌 때 까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 우너소와 연 결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
      indegree[i] -= 1
      # 새롭게 집입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  # 위상 정렬을 수행한 결과 출력
  for i in result:
    print(i, end = " ")

topology_sort()


# 풀이 참고 - https://developmentdiary.tistory.com/465
# 위상정렬, DP

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N, K = map(int, input().split()) # 건물 수, 건물간의 건설순서 규칙
  building = [0] + list(map(int, input().split())) # 각 건물들의 건설 시간
  tree = [[] for _ in range(N + 1)] # 건설 순서 규칙
  inDegree = [0 for _ in range(N + 1)] # 위상 정렬에서 사용할 진입 차수
  DP = [0 for _ in range(N + 1)] # 해당 건물 건설까지 걸리는 시간

  for _ in range(K):  # 건설 규칙 저장
    a, b = map(int, input().split())
    tree[a].append(b)
    inDegree[b] += 1

  q = deque()
  for i in range(1, N + 1): # 진입차수가 0인 빌딩 찾아 큐에 넣기
    if inDegree[i] == 0:
      q.append(i)
      DP[i] = building[i]

  while q:
    a = q.popleft()
    for i in tree[a]:
      inDegree[i] -= 1 #진입차수 줄임
      DP[i] = max(DP[i], DP[a] + building[i]) # DP를 이용해 건설 시간 갱신
      if inDegree[i] == 0:
        q.append(i)
    
  answer = int(input())
  print(DP[answer])