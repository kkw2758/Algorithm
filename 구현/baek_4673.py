

visited = [False] * 10001

for i in range(1, 10001):
  d_n = sum(map(int, list(str(i))))
  d_n += i
  if d_n <= 10000 and not visited[d_n]:
    visited[d_n] = True

for n in range(1, 10001):
  if not visited[n]:
    print(n)