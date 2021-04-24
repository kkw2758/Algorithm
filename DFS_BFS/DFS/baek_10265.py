n, k = map(int, input().split())
graph = [0] + list(map(int, input().split()))
visited = [0 for _ in range(n + 1)]


print(graph)



def dfs_stack(start_vertex):
    stack = [start_vertex]
    cycle = []
    while stack:
        now_vertex = stack.pop()
        # 방문처리
        visited[now_vertex] = 1
        # 사이클에 방문한 노드 추가
        cycle.append(now_vertex)

        next_vertex = graph[now_vertex]
        if not visited[next_vertex]:
            stack.append(next_vertex)
        
        else: # 다음 경로를 이미 갔을 경우
            if next_vertex in cycle:
                return cycle[cycle.index(next_vertex):]