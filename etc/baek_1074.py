# 2022/09/04 Baek 1074


from re import L


N, r, c = map(int, input().split())

graph = [[0] * (2 ** N + 1) for _ in range(2 ** N + 1)]
# def func(n, first, start_x, start_y):
#   if n == 1:
#     graph[start_x][start_y] = first
#     graph[start_x][start_y + 1] = first + 1
#     graph[start_x + 1][start_y] = first + 2
#     graph[start_x + 1][start_y + 1] = first + 3
#   else:
#     func(n - 1, first, start_x, start_y, start_x + 2**(n-1) - 1, start_y + 2**(n-1) - 1 )
#     func(n - 1, first + 4 ** (n - 1), start_x, start_y + 2**(n-1), start_x + 2**(n-1), start_y + 2 ** n - 1)
#     func(n - 1, first + 4 ** (n - 1) * 2, start_x + 2**(n-1), start_y, start_x + 2 ** n - 1, start_y + 2**(n-1) - 1 )
#     func(n - 1, first + 4 ** (n - 1) * 3, start_x + 2**(n-1), start_y + 2**(n-1), start_x + 2 ** n - 1, start_y + 2 ** n - 1)

def func(n, first, start_x, start_y):
  if n == 1:
    graph[start_x][start_y] = first
    graph[start_x][start_y + 1] = first + 1
    graph[start_x + 1][start_y] = first + 2
    graph[start_x + 1][start_y + 1] = first + 3
  else:
    func(n - 1, first, start_x, start_y)
    func(n - 1, first + 4 ** (n - 1), start_x, start_y + 2**(n-1))
    func(n - 1, first + 4 ** (n - 1) * 2, start_x + 2**(n-1), start_y)
    func(n - 1, first + 4 ** (n - 1) * 3, start_x + 2**(n-1), start_y + 2**(n-1))


func(N, 0, 1, 1)
# for _ in graph:
#   print(_)
print(graph[r+1][c+1])