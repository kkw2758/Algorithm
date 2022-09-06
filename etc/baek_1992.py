# 2022/09/05 Baek 1992

N = int(input())
graph = []
for _ in range(N):
  graph.append(list(map(int, list(input()))))

def check(n, start_x, start_y):
  if graph[start_x][start_y] == 0:
    for row in range(n):
      for col in range(n):
        if graph[start_x + row][start_y + col] == 1:
          return -1
    return 0
  else:
    for row in range(n):
      for col in range(n):
        if graph[start_x + row][start_y + col] == 0:
          return -1
    return 1

def quad_tree(n, start_x, start_y):
  check_result = check(n, start_x, start_y)
  if check_result == 0:
    return "0"
  elif check_result == 1:
    return "1"
  else:
    result = "("
    result += quad_tree(n//2, start_x, start_y)
    result += quad_tree(n//2, start_x, start_y + n//2)
    result += quad_tree(n//2, start_x + n//2, start_y)
    result += quad_tree(n//2, start_x + n//2, start_y + n//2)
    result += ")"
    return result

print(quad_tree(N,0,0))