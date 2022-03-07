# from collections import deque

# n, m, k, x = map(int, input().split())

# temp = [[] for _ in range(n + 1)]
# visited = [False for _ in range(n + 1)]

# for _ in range(m):
#     i, j = map(int, input().split())
#     temp[i].append(j)


# queue = deque()
# queue.append(x)
# visited[x] = True
# distance = 0
# result = []

# while queue:
#     for i in range(len(queue)):
#         now_node = queue.popleft()
#         if distance == k:
#             result.append(now_node)
#         for next_node in temp[now_node]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#     distance += 1

# if result:
#     for member in result:
#         print(member)
# else:
#     print(-1)


# # while queue:
# #     for i in range(len(queue)):
# #         node = queue.popleft()
# #         if distance == k:
# #             result.append(node)
# #         for idx in range(len(temp[node])):
# #             if not visited[temp[node][idx]]:
# #                 visited[temp[node][idx]] = True
# #                 queue.append(temp[node][idx])
# #     distance += 1


# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# distance = [-1] * (n + 1)
# distance[x] = 0

# q = deque([x])
# while q:
#     now = q.popleft()
#     for next_node in graph[now]:
#         if distance[next_node] == -1:
#             distance[next_node] = distance[now] + 1
#             q.append(next_node)

# check = False
# for i in range(1, n + 1):
#     if distance[i] == k:
#         print(i)
#         check = True

# if check == False:
#     print(-1)

from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])

while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)