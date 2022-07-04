import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n = int(input())
planet_list = []
for i in range(n):
  x, y, z = map(int, input().split())
  planet_list.append((x, y, z))

edges = []

for i in range(n):
  x1, y1, z1 = planet_list[i]
  for j in range(i + 1, n):
    x2, y2, z2 = planet_list[j]
    cost = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
    edges.append((cost, i, j))

edges.sort()

parent = [0] * n

for i in range(n):
  parent[i] = i

min_cost = 0

for edge in edges:
  cost, x, y = edge
  if find_parent(parent, x) != find_parent(parent, y):
    union_parent(parent, x, y)
    min_cost += cost

print(min_cost)

'''
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''