# 2022/09/06 Baek 7662

# 최소힙과 최대힙을 적절한 방법으로 동기화해서 처리해야함
# 시간 초과 코드
# q1 - 최소힙/ q2 - 최대힙
# 동기화 과정에서 q1이나 q2를 아예 초기화 한다음에 heapq.heappush를 실행해 시간초과
import heapq
from multiprocessing import heap
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
  K = int(input())
  q1 = []
  q2 = []

  for _ in range(K):
    symbol, integer = input().split()
    integer = int(integer)
    if symbol == "I":
      heapq.heappush(q1, integer)
      heapq.heappush(q2, -integer)
    elif symbol == "D":
      if integer == 1:
        if len(q2) == 0:
          continue
        heapq.heappop(q2)
        q1 = []
        for i in q2:
          heapq.heappush(q1, -i)
      elif integer == -1:
        if len(q1) == 0:
          continue
        heapq.heappop(q1)
        q2 = []
        for i in q1:
          heapq.heappush(q2, -i)

  q1 = set(q1)
  q2 = set([-member for member in q2])
  result = list(q1 & q2)
  if result:
    print(max(result), min(result))
  else:
    print("EMPTY")

# 인터넷 참고 풀이
# 힙에 값을 추가하는 과정에서 id 값을 넣어주어 이 id값을 이용하여 최대힙과 최소힙을 동기화
import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  max_heap, min_heap = [], []
  visit = [False] * 1000001

  order_num = int(input())

  for key in range(order_num):
    symbol, integer = input().split()
    if symbol == "I":
      heapq.heappush(min_heap, (int(integer), key))
      heapq.heappush(max_heap, (int(integer) * -1, key))
      visit[key] = True
    
    elif symbol == "D":
      if integer == "-1":
        while min_heap and not visit[min_heap[0][1]]:
          heapq.heappop(min_heap)
        if min_heap:
          visit[min_heap[0][1]] = False
          heapq.heappop(min_heap)
      elif integer == "1":
        while max_heap and not visit[max_heap[0][1]]:
          heapq.heappop(max_heap)
        if max_heap:
          visit[max_heap[0][1]] = False
          heapq.heappop(max_heap)

  while min_heap and not visit[min_heap[0][1]]:
    heapq.heappop(min_heap)
  while max_heap and not visit[max_heap[0][1]]:
    heapq.heappop(max_heap)

  if min_heap and max_heap:
    print(-max_heap[0][0], min_heap[0][0])
  else:
    print("EMPTY")