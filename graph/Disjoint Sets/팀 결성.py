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

# n, m = map(int, input().split())
# parent = [0] * (n + 1)
# results = []

# for i in range(1, n + 1):
#     parent[i] = i

# for _ in range(m):
#     mode, a, b = map(int, input().split())
#     if mode == 1:
#         if find_parent(parent, a) == find_parent(parent, b):
#             # print("YES")
#             results.append("YES")
#         else:
#             # print("NO")
#             results.append("NO")
#     elif mode == 0:
#         union_parent(parent, a, b)

# for result in results:
#     print(result)

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

NO
NO
YES
'''

n, m = map(int, input().split())

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
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = []
for _ in range(m):
    mode, a, b = map(int, input().split())
    if mode == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")

for x in result:
    print(x)