# 2022/11/21 Baek 1253

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

cnt = 0

for i in range(N):
  left = 0
  right = N - 2
  current = numbers.pop(i)
  
  while left < right:
    sum = numbers[left] + numbers[right]
    if sum == current:
      cnt += 1
      break
    elif sum < current:
      left += 1
    else:
      right -= 1
  numbers.insert(i, current)

print(cnt)


import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

cnt = 0

for i in range(N):
  temp = numbers[:i] + numbers[i + 1:]
  left = 0
  right = N - 2
  
  while left < right:
    sum = temp[left] + temp[right]
    if sum == numbers[i]:
      cnt += 1
      break
    elif sum < numbers[i]:
      left += 1
    else:
      right -= 1
  
print(cnt)