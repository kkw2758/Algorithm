# 2022/12/26 Baek 1205

N, S, P = map(int, input().split())

if N == 0:
  print(1)
else:
  scores = list(map(int, input().split()))
  if N == P and scores[-1] >= S:
    print(-1)
  else:
    result = N + 1
    for i in range(N):
      if scores[i] <= S:
        result = i + 1
        break
    print(result)