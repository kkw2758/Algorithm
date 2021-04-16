'''
import sys
sys.setrecursionlimit(100000)

def dfs(start, end):
    stack = []
    stack.append(graph[start - 1])
    cnt = 1

    while stack:
        now, destination = stack.pop()
 
        visited[now - 1] = True

        if destination == end:
            return cnt

        if not(visited[destination - 1]):
            stack.append((destination, graph[destination - 1][1]))
            cnt += 1
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    choice_number = list(map(int,input().split()))
    graph = []
    for idx in range(len(choice_number)):
        graph.append((idx + 1, choice_number[idx]))
    
    visited = [False] * n
    result = n
    for x in range(1, n + 1):
        #visited = [False] * n
        #print("-",x,dfs(x,x))
        result -= dfs(x,x)
        #if dfs(x,x):
        #    result -= 1
            #print("-",x, result)

    print(result)
'''
'''
import sys
sys.setrecursionlimit(100000)

def dfs(start, end):
    stack = []
    stack.append(graph[start - 1])
    
    while stack:
        now, destination = stack.pop()
        visited[now - 1] = True

        if destination == end:
            return True

        if not(visited[destination - 1]):
            stack.append((destination, graph[destination - 1][1]))

    return False

t = int(input())
for _ in range(t):
    n = int(input())
    choice_number = list(map(int,input().split()))
    graph = []
    for idx in range(len(choice_number)):
        graph.append((idx + 1, choice_number[idx]))


    result_list = []
    for x in range(1, n + 1):
        if x not in result_list:
            visited = [False] * n
            if dfs(x,x):
                for y in range(len(visited)):
                    if visited[y]:
                        result_list.append(y + 1)
                        
    print(n - len(result_list))
    '''
'''



import sys
sys.setrecursionlimit(100000)

def dfs(start, end):
    stack = []
    stack.append((start, choice_number[start - 1]))
    
    while stack:
        now, destination = stack.pop()
        visited[now - 1] = True

        dp[now][destination] = 1
        
        if destination == end:
            return True

        if not(visited[destination - 1]):
            stack.append((destination, choice_number[destination - 1]))
            dp[now][choice_number[destination -1]] = 1
    return False

t = int(input())
for _ in range(t):

    
    
    n = int(input())
    dp = [[0] * n] * n
    choice_number = list(map(int,input().split()))

    result_list = []
    for x in range(1, n + 1):
        if x not in result_list:
            visited = [False] * n
            if dfs(x,x):
                for y in range(len(visited)):
                    if visited[y]:
                        result_list.append(y + 1)
                        
    print(n - len(result_list))


'''
'''
import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]
    
    if visited[number]: #방문가능한 곳이 끝났는지
        if number in cycle: #사이클 가능 여부
            result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸
            #print(result)
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N #방문 여부
    result = []
    
    for i in range(1, N+1):
        if not visited[i]: #방문 안한 곳이라면
            cycle = []
            dfs(i) #DFS 함수 돌림
            print(i,result)
            
    print(N - len(result)) #팀에 없는 사람 수
'''


'''
import sys
sys.setrecursionlimit(100000)

def dfs(start, end):
    stack = []
    stack.append(graph[start - 1])
    cycle = []

    while stack:
        now, destination = stack.pop()
        visited[now - 1] = True
        cycle.append(now)

        if destination == end:
            return True

        if not(visited[destination - 1]):
            stack.append((destination, graph[destination - 1][1]))
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    choice_number = list(map(int,input().split()))
    graph = []
    for idx in range(len(choice_number)):
        graph.append((idx + 1, choice_number[idx]))
    
    visited = [False] * n
    result = n
    for x in range(1, n + 1):
        #visited = [False] * n
        #print("-",x,dfs(x,x))
        result -= dfs(x,x)
        #if dfs(x,x):
        #    result -= 1
            #print("-",x, result)

    print(result)
'''
import sys
sys.setrecursionlimit(100000)

def dfs(start_node):
    stack = []
    stack.append(graph[start_node - 1])
    cycle = []

    while stack:
        now, destination = stack.pop()
        visited[now -1] = True
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
            
