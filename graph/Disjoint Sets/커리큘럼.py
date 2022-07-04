# from collections import deque

# n = int(input())
# graph = [[] for _ in range(n + 1)]
# indegree = [0] * (n + 1)

# for idx in range(1, n + 1):
#     temp = list(map(int, input().split()))
#     graph[idx].append(temp[0])
#     for i in temp[1:-1]:
#         graph[i].append(idx)
#         indegree[idx] += 1

# def topology_sort():
#     result = []
#     q = deque()

#     for i in range(1, n + 1):
#         if indegree[i] == 0:
#             q.append((i, 0))

#     while q:
#         now, ago_value = q.popleft()
#         now_value = ago_value + graph[now][0]
#         result.append(now_value)

#         for i in graph[now][1:]:
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 q.append((i, now_value))

#     return result

# result = topology_sort()
# for _ in result:
#     print(_)

# '''
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 10
# 20
# 14
# 18
# 17
# '''

# # 문제 해설
# # 위상 정렬의 응용 문제

# from collections import deque
# import copy

# v = int(input())
# indegree = [0] * (v + 1)

# graph = [[] for i in range(v + 1)]
# time = [0] * (v + 1)

# for i in range(1, v + 1):
#     data = list(map(int, input().split()))
#     time[i] = data[0]
#     for x in data[1:-1]:
#         indegree[i] += 1
#         graph[x].append(i)

# def sol_topology_sort():
#     result = copy.deepcopy(time)
#     q = deque()

#     for i in range(1, v + 1):
#         if indegree[i] == 0:
#             q.append(i)

#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             result[i] = max(result[i], result[now] + time[i])
#             indegree[i] -= 1
            
#             if indegree[i] == 0:
#                 q.append(i)

#     for i in range(1, v + 1):
#         print(result[i])

# sol_topology_sort()

from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
times = [0]

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    time = temp[0]
    times.append(time)
    before_course = temp[1:]

    for x in range(len(before_course) - 1):
        graph[before_course[x]].append(i)
        indegree[i] += 1


def topology_sort():
    q = deque()
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
        result[i] = times[i]
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''