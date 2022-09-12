# 2022/09/12 Baek 9019

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
  visited[start] = True
  q = deque()
  q.append(start)

  while q:
    n = q.popleft()
    if n == end:
      return courses[n]
    for i in ["D", "S", "L", "R"]:
      if i == "D":
        new_n = (n * 2) % 10000
      elif i == "S":
        new_n = (n - 1) % 10000
      elif i == "L":
        d1 = n // 1000
        d234 = (n % 1000) * 10
        new_n = d234 + d1
      elif i == "R":
        d4 = (n % 10) * 1000
        d123 = (n - n % 10) // 10
        new_n = d4 + d123

      if not visited[new_n]:
        visited[new_n] = True
        courses[new_n] = courses[n] + i
        q.append(new_n)


T = int(input())
for _ in range(T):
  A, B = map(int, input().split())
  visited = [False] * 10000
  courses = [""] * 10000
  print(bfs(A, B))