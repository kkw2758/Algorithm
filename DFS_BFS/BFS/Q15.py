from collections import deque
import sys

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
temp = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    temp[i].append(j)


queue = deque()
queue.append(x)
visited[x] = True
distance = 0
result = []

while queue:
    length = len(queue)
    for i in range(length):
        now_node = queue.popleft()
        if distance == k:
            result.append(now_node)
        for next_node in temp[now_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    distance += 1

result.sort()

if result:
    for member in result:
        print(member)
else:
    print(-1)




# from collections import deque
# import sys

# input = sys.stdin.readline

# N, M, K, X = map(int, input().split())
# distances = [-1 for _ in range(N + 1)]
# board = [[] for _ in range(N + 1)]

# for _ in range(M):
#     start, end = map(int, input().split())
#     board[start].append(end)

# q = deque([X])
# distances[X] = 0
# while q:
#     now = q.popleft()
#     for next_node in board[now]:
#         if distances[next_node] == -1:
#             distances[next_node] = distances[now] + 1
#             q.append(next_node)


# check = False
# for i in range(1, len(distances)):
#     if distances[i] == K:
#         print(i)
#         check = True

# if not check:
#     print(-1)