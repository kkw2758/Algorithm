# 2022/09/03 Baek 17219

N = int(input())
time = list(map(int, input().split()))
time.sort()

result = 0
for i in range(1, len(time) + 1):
  for j in range(i):
    result += time[j]

print(result)