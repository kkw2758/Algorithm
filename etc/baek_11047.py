# 2022/09/03 Baek 11047

N, K = map(int, input().split())
coin_value = []

for _ in range(N):
  coin_value.append(int(input()))

coin_value.sort(reverse=True)

cnt = 0
for i in range(N):
  if K >= coin_value[i]:
    cnt += K // coin_value[i]
    K = K % coin_value[i]
    if K == 0:
      break

print(cnt)