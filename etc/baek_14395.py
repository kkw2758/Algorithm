# 2022/11/30 Baek 14395

from collections import deque

def bfs(start):
  visited = set()
  queue = deque()
  queue.append((start, ""))
  visited.add(start)

  while queue:
    now, result = queue.popleft()
    if now == t:
      return result
    if now != 0:
      for idx, value in enumerate([now * now, now + now, 1]):
        if 1 <= value <= 1000000000 and value not in visited:
        # if 1 <= value <= t and value not in visited:
          if idx == 0:
            queue.append((value, result + "*"))
            visited.add(value)
          elif idx == 1:
            queue.append((value, result + "+"))
            visited.add(value)
          elif idx == 2:
            queue.append((value, result + "/"))
            visited.add(value)
  return - 1


s, t = map(int, input().split())
result = str(int(1e9))
if s == t:
  print(0)
else:
  print(bfs(s))
