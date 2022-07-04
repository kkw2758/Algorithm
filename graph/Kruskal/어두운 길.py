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

N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(1, N + 1):
  parent[i] = i

edges = []
total_cost = 0
for i in range(M):
  x, y, z = map(int, input().split())
  edges.append((z, x, y))
  total_cost += z

edges.sort()

min_cost = 0

for edge in edges:
  cost, x, y = edge
  if find_parent(parent, x) != find_parent(parent, y):
    union_parent(parent, x, y)
    min_cost += cost

# print("Total cost : {}".format(total_cost))
# print("Min cost : {}".format(min_cost))
print(total_cost - min_cost)


'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''