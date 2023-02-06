S = int(input())

cnt = 0
sum = 0
while True:
  if sum > S:
    break
  cnt += 1
  sum += cnt

print(cnt - 1)