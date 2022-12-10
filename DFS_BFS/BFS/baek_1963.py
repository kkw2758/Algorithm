# 2022/12/09 baek 1963

import math
from collections import deque

def is_prime_number(x):
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

T = int(input())

for _ in range(T):
  result = int(1e9)
  start, end = map(int, input().split())
  
  if start == end:
    result = 0
    print(result)
    continue

  q = deque()
  q.append((start, 0))
  visited = set()
  visited.add(start)

  while q:
    now, cnt = q.popleft()
    if now == end:
      result = cnt
      break
    # i 번째 자리
    now_list = list(str(now))
    for i in range(4):
      # j 로 바꿈
      for j in range(10):
        new_number = now_list[:i] + [str(j)] + now_list[i + 1:]
        new_number = int("".join(new_number))
        if (new_number not in visited) and (new_number >= 1000) and is_prime_number(new_number):
          q.append((new_number, cnt + 1))
          visited.add(new_number)

  if result == int(1e9):
    print("Impossible")
  else:
    print(result)