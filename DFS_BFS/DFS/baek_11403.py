#나의 풀이
def find_index(li, target):
    result = []
    for idx in range(len(li)):
        if li[idx] == target:
            result.append(idx)

    return result

def dfs_stack(start_node):
    stack = []
    stack += find_index(board[start_node],1)

    while stack:
        node = stack.pop()
        #방문 처리
        visited[node] = True
        result[start_node][node] = 1

        for idx in find_index(board[node], 1):
            if not(visited[idx]):
                stack.append(idx)



n = int(input())

board = [[0] * (n + 1)]
for _ in range(n):
    board.append([0] + list(map(int,input().split())))

result = [[0] * (n + 1) for _ in range(n + 1)]





for start_node in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs_stack(start_node)
    

for row in range(1, n + 1):
    for col in range(1, n + 1):
        print(result[row][col], end = ' ')
    print('')




# 문제에서 n x n 행렬을 입력받는데 문제를 푸는데있어서 핵심은 i에서 j으로 가는 간선이 어디에 있는지만 알면됨
# 따라서 i행에서 j으로 가는 경로가 있을때 edge리스트의 i행에 j값을 추가해주는식으로 공간 절약함.
'''

#재귀함수를 이용한 시간을 단축하는 풀이
def dfs_recursive(start_node):
    for node in edge[start_node]:
        if not visited[node]:
            visited[node] = 1
            dfs_recursive(node)

n = int(input())
edge = [[] for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]:
            edge[i].append(j)

for i in range(n):
    visited = [0 for row in range(n)]
    dfs_recursive(i)
    print(' '.join(map(str, visited)))



#스택을 이용한 시간을 단축하는 풀이
def dfs_stack(start_node):
    stack = [start_node]

    while stack:
        start_node = stack.pop()
        for node in edge[start_node]:
            if not visited[node]:
                visited[node] = 1
                stack.append(node)

n = int(input())
edge = [[] for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]:
            edge[i].append(j)

for i in range(n):
    visited = [0 for row in range(n)]
    dfs_stack(i)
    print(' '.join(map(str, visited)))

'''