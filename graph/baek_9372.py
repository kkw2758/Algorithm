# 2023/01/16 Baek 9372

T = int(input())

def dfs():
  stack = []
  # node_number, cnt
  stack.append(1)
  
  visited = [-1] * (N + 1)
  visited[1] = 0
  result = 0
  while stack:
    node_number= stack.pop()
    for next_node in Tree[node_number]:
      if visited[next_node] == -1:
        visited[next_node] = 0
        stack.append(next_node)
        result += 1

  return result

for _ in range(T):
  N, M = map(int, input().split())
  Tree = [[] for _ in range(N + 1)]
  
  for _ in range(M):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

  print(dfs())
