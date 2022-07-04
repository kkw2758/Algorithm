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

n, m = map(int, input().split())
graph = [[]]

for _ in range(n):
  graph.append([0] + list(map(int, input().split())))

plan_list = list(set(map(int, input().split())))

parent = [0] * (n + 1)

for i in range(1, n+1):
  parent[i] = i
  

for i in range(1, n + 1):
  for j in range(i + 1, n + 1):
    if graph[i][j] == 1:
      union_parent(parent, i, j)


def is_possible(plan_list, parent):
  first = parent[plan_list[0]]
  for i in range(1,len(plan_list)):
    if first != parent[plan_list[i]]:
      return "NO"
  
  return "YES"

print(is_possible(plan_list, parent))
'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''