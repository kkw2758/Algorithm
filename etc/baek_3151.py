# 2022/11/20 Baek 3151
# 브루트 포스 - 조합 >> 시간이 너무 오래걸림
from itertools import combinations
N = int(input())

scores = list(map(int, input().split()))
candidates = combinations(scores, 3)
cnt = 0

for candidate in candidates:
  if sum(candidate) == 0:
    cnt += 1

print(cnt)


# 투포인터
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

for i in range(N - 2):
  left, right = i + 1, N - 1
  goal = -arr[i]
  mx_idx = N

  while left < right:
    tmp = arr[left] + arr[right]

    if tmp < goal:
      left += 1

    elif tmp > goal:
      right -= 1

    else:
      if arr[left] == arr[right]:
        ans += right - left
      else:
        if mx_idx > right:
          mx_idx = right
          while mx_idx >= 0 and arr[mx_idx - 1] == arr[right]:
            mx_idx -= 1

        ans += right - mx_idx + 1
      left += 1

print(ans)


# 투포인터 카운터 사용 풀이
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = Counter(arr)
ans = 0

for i in range(N - 2):
  left = i + 1
  right = N - 1
  while left < right:
    sum = arr[left] + arr[right] + arr[i]
    if sum == 0:
      if arr[left] == arr[right]:
        ans += right - left
      else:
        ans += cnt[arr[right]]
      left += 1
    elif sum > 0:
      right -= 1
    else:
      left += 1

print(ans)

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i in range(N - 2):
  left = i + 1
  right = N - 1
  while left < right:
    sum = arr[left] + arr[right] + arr[i]
    if sum == 0:
      if arr[left] == arr[right]:
        answer += right - left
      else:
        idx = bisect_left(arr, arr[right])
        answer += right - idx + 1
      left += 1

    elif sum > 0:
      right -= 1
    else:
      left += 1

print(answer)