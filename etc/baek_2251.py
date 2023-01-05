# 2023/01/05 Baek 2251

import sys
input = sys.stdin.readline

capacity = list(map(int, input().split()))

visited = []

def dfs():
  stack = []
  stack.append([0, 0, capacity[2]])
  visited.append([0, 0, capacity[2]])

  while stack:
    status = stack.pop()
    if status[0] == 0:
      if status not in visited:
        visited.append(status)

    for i in range(3):
      for j in range(3):
        if i == j or status[j] == capacity[j]:
          continue
        temp_status = status[:]
        if temp_status[i] + temp_status[j] > capacity[j]:
          temp_status[i], temp_status[j] = temp_status[i] - (capacity[j] - temp_status[j]), capacity[j]
        else:
          temp_status[i], temp_status[j] = 0, temp_status[j] + temp_status[i]
        
        if temp_status not in visited:
          visited.append(temp_status)
          stack.append(temp_status)

dfs()
result = []
for a, b, c in visited:
  if a == 0 and c not in result:
    result.append(c)

result.sort()
for i in result:
  print(i,end = " ")