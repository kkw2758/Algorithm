# 2023/02/27 Baek 2628

w, h = map(int, input().split())
n = int(input())

wide = [0, w]
height = [0, h]

for _ in range(n):
  status, number = map(int, input().split())
  if status == 0:
    height.append(number)
  else:
    wide.append(number)

wide.sort()
height.sort()
max_w = 0
max_h = 0
for i in range(1, len(wide)):
  max_w = max(max_w, wide[i] - wide[i - 1])

for i in range(1, len(height)):
  max_h = max(max_h, height[i] - height[i - 1])

print(max_w * max_h)