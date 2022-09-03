# 2022/09/04 Baek 2630

N = int(input())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

def check(graph):
  global white_cnt, blue_cnt
  if graph[0][0] == 1:
    for row in range(len(graph)):
      for col in range(len(graph[0])):
        if graph[row][col] == 0:
          return False
    blue_cnt += 1
    return True
  else:
    for row in range(len(graph)):
      for col in range(len(graph[0])):
        if graph[row][col] == 1:
          return False
    white_cnt += 1
    return True

white_cnt = 0
blue_cnt = 0

def count_paper(graph):
  result = check(graph)
  if result == True:
    return
  count_paper([i[:len(graph)//2] for i in graph[:len(graph)//2]])
  count_paper([i[len(graph)//2:] for i in graph[:len(graph)//2]])
  count_paper([i[:len(graph)//2] for i in graph[len(graph)//2:]])
  count_paper([i[len(graph)//2:] for i in graph[len(graph)//2:]])

count_paper(graph)
print(white_cnt)
print(blue_cnt)
