# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if b > a:
#         parent[b] = a
#     else:
#         parent[a] = b

# edges = []
# result = []
# n, m = map(int, input().split())
# parent = [0] * (n + 1)

# for i in range(1, n + 1):
#     parent[i] = i

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     edges.append((c, a, b))

# edges.sort()

# for edge in edges:
#     c, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result.append(c)

# print(sum(result) - max(result))



n, m = map(int, input().split())

edges = []

for x in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

result = 0
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)

'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''