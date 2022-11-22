# 2022/11/22 Baek 2143

import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))

A_sum = []
for i in range(len(A)):
  s = 0
  for j in range(i, len(A)):
    s += A[j]
    A_sum.append(s)

A_count = Counter(A_sum)
A = list(A_count)

M = int(input())
B = list(map(int, input().split()))

B_sum = []
for i in range(len(B)):
  s = 0
  for j in range(i, len(B)):
    s += B[j]
    B_sum.append(s)

B_count = Counter(B_sum)

ans = 0
for i in range(len(A)):
  ans += A_count[A[i]] * B_count[T - A[i]]

print(ans)


# upper_bound, lower_bound 이용
import sys
from collections import Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))

A_sum = []
for i in range(len(A)):
  s = 0
  for j in range(i, len(A)):
    s += A[j]
    A_sum.append(s)

A_count = Counter(A_sum)

M = int(input())
B = list(map(int, input().split()))

B_sum = []
for i in range(len(B)):
  s = 0
  for j in range(i, len(B)):
    s += B[j]
    B_sum.append(s)

B_sum.sort()

ans = 0
for i in range(len(A_sum)):
  l = bisect_left(B_sum, T - A_sum[i])
  r = bisect_right(B_sum, T - A_sum[i])
  ans += r - l

print(ans)


# A_count 만 만들기
import sys
from collections import Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))

A_sum = []
for i in range(len(A)):
  s = 0
  for j in range(i, len(A)):
    s += A[j]
    A_sum.append(s)

A_count = Counter(A_sum)

M = int(input())
B = list(map(int, input().split()))

ans = 0
for i in range(len(B)):
  for j in range(i, len(B)):
    ans += A_count[T - sum(B[i : j + 1])]

print(ans)