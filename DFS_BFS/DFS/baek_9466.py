'''
#스택을 이용해서 구현을 했는데 메모리는 절약되는반면 시간이 오래걸림..
import sys
sys.setrecursionlimit(100000)

def dfs(start_node):
    stack = []
    stack.append(graph[start_node - 1])
    cycle = []

    while stack:
        now, destination = stack.pop()
        visited[now - 1] = True
        cycle.append(now)

        if not(visited[destination - 1]):
            stack.append((destination, graph[destination - 1][1]))
        else:
            if destination in cycle:
                return cycle[cycle.index(destination):]

    return []

t = int(input())
for _ in range(t):
    n = int(input())
    choice_number = list(map(int,input().split()))
    graph = []
    for idx in range(len(choice_number)):
        graph.append((idx + 1, choice_number[idx]))
    
    visited = [False] * n
    result = []
    for x in range(1, n + 1):
        if not(visited[x - 1]):
            tmp = dfs(x)
            if tmp:
                result += tmp

    print(n - len(result))
'''


'''
#스택을 이용한 빠른 풀이
#시작 정점에서 방문할수있는 모든 정점을 방문하거나 사이클이 되는곳까지만 방문
import sys
sys.setrecursionlimit(100000)

def dfs_stack(start_node):
    stack = [start_node]
    global result
    while stack:
        now_node = stack.pop()
        # 방문처리 및 사이클처리
        visited[now_node] = 1
        cycle.append(now_node)
        next_node = matrix[now_node]
        
        if not visited[next_node]:
            stack.append(next_node)
        else:
            if next_node in cycle:
                result += cycle[cycle.index(next_node):] 


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    matrix = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] + [0] * n


    result = []
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs_stack(i)

    print(n - len(result))
'''


'''
#시작 정점에서 갈 수 있는 모든 정점을 탐색하기도전에 사이클여부를 확인하고있으므로 불필요 연산을 많이 하게됨.
import sys
sys.setrecursionlimit(1000000)

def dfs_recursive(start_vertex):
    result = []
    if start_vertex in cycle:
        return cycle[cycle.index(start_vertex):]

    if not visited[start_vertex]:
        visited[start_vertex] = 1
        cycle.append(start_vertex)
        result += dfs_recursive(matrix[start_vertex])

    return result

t = int(sys.stdin.readline())


for _ in range(t):
    n = int(sys.stdin.readline())

    matrix = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] + [0] * n

    result = 0
    #cycle = []
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            result += len(dfs_recursive(i))


    print(n - result)
'''


'''
import sys
sys.setrecursionlimit(1000000)

def dfs_recursive(start_vertex):
    global result
    visited[start_vertex] = 1
    cycle.append(start_vertex)

    if not visited[matrix[start_vertex]]:
        dfs_recursive(matrix[start_vertex])
    else:
        if matrix[start_vertex] in cycle:
            result += cycle[cycle.index(matrix[start_vertex]):]
            return



t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    matrix = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] + [0] * n


    result = []
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs_recursive(i)


    print(n - len(result))
'''