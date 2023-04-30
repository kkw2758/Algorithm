# 2023/04/27 Baek 16953

import sys

A, B = map(int, input().split())

# 1을 수의 가장 오른쪽에 추가하거나 2를 곱하거나
# 문제의 입출력예시를 보니 그리디 알고리즘은 아닌 것 같다.

# 완전탐색 백트래킹 같음
result = int(1e9)
def back(number, cnt):
    global result
    if number > B:
        return
    if number == B:
        # print("A")
        result = min(result, cnt + 1)
        
    back(number * 2, cnt + 1)
    back(int(str(number) + "1"), cnt + 1)
    
back(A, 0)
if result == int(1e9):
    print(-1)
else:
    print(result)
    
#------------------------------------------------
# BFS를 이용한 풀이
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append((B, 1))
  while q:
    v, cnt = q.popleft()
    if v == A:
      return cnt
    if v > 1:
      d = []
      if not v % 2: # 2로 나누어 떨어지면
        d.append((v // 2))
      if str(v)[-1] == '1': # 마지막이 1로 끝이난다면
        d.append(int(str(v)[:-1]))
      for value in d:
        q.append((value, cnt+1))
  return -1

A, B = map(int,input().split())
res = bfs()
print(res)

#------------------------------------------------
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append((A, 0))
  while q:
    v, cnt = q.popleft()
    if v == B:
      return cnt + 1
    if v < B:
      q.append((int(str(v) + "1"), cnt + 1))
      q.append((v * 2, cnt + 1))
  return -1

A, B = map(int,input().split())
res = bfs()
print(res)