import time

def find_min_idx(arr):
  min_idx = 0
  for i in range(len(arr)):
    if arr[min_idx] > arr[i]:
      min_idx = i
  return min_idx

def find_n_ugly_number(n):
  if n == 1:
    return 1
  dp = [1]
  for i in range(1, n):
    now_idx = find_min_idx(dp)
    now_value = dp[now_idx]

    for j in range(len(dp)):
      dp.append(now_value * 2)
      dp.append(now_value * 3)
      dp.append(now_value * 5)

    dp.pop(now_idx)
    dp = list(set(dp))

  return min(dp)
start = time.time()
n = int(input())
print(find_n_ugly_number(n))
end = time.time()
print("Time = {}".format(end - start))



n = int(input())
start = time.time()
ugly = [0] * n
ugly[0] = 1
i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
  ugly[l] = min(next2, next3, next5)
  if ugly[l] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[l] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[l] == next5:
    i5 += 1
    next5 = ugly[i5] * 5

print(ugly[n-1])
end = time.time()
print("Time = {}".format(end - start))