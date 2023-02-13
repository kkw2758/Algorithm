# N, M = map(int, input().split())

# left_side = []
# for _ in range(N - 1):
#   left_side.append(int(input()))
# bottom = list(map(int, input().split()))

# flag = False

# for i in range(len(left_side)):
#   if left_side[i] == 0:
#     print(i + 1, 1)
#     flag = True
#     break
# if flag == False:
#   for i in range(len(bottom)):
#     if bottom[i] == 0:
#       print(N, i + 1)
#       flag = True
#       break

# if flag == False:
#   print(N - min(bottom), min(left_side) + 1)



# 2
N, M = map(int, input().split())
papers = list(set([i for i in range(1, N + 1)]) - set(list(map(int, input().split()))))
papers.sort()

result = 0
before = []
for i in range(len(papers)):
  if not before or papers[i] - before[-1] <= 3:
    before.append(papers[i])
  else:
    result += (before[-1] - before[0] + 1) *2 + 5
    before = [papers[i]]

if before:
  result += (before[-1] - before[0] + 1) *2 + 5
  
print(result)