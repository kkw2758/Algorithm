# 2022/09/04 Baek 18870

from bisect import bisect_left

N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(set(numbers))

for number in numbers:
  print(bisect_left(sorted_numbers, number), end = " ")

def solve(arr):
  sorted_arr = sorted(set(arr))
  d = {x: idx for idx, x in enumerate(sorted_arr)}
  return [d[x] for x in arr]

N = int(input())
arr = list(map(int, input().split()))
print(' '.join(map(str, solve(arr))))