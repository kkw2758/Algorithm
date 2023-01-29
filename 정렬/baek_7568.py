# 2023/01/30 Baek 7568

N = int(input())
people = []
for _ in range(N):
  x, y = map(int, input().split())
  people.append((x, y))

for i in range(N):
  x, y = people[i]
  cnt = 0
  for j in range(N):
    p, q = people[j]
    if i == j:
      continue
    if x < p and y < q:
      cnt += 1
  print(cnt + 1, end = " ")

    
