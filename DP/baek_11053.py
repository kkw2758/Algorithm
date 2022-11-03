# 2021/06/15 Baek 11053

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

#dp를 사용하지않은 기발한 풀이!
import sys

read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().strip().split()))
sol = [arr[0]]

for i in range(1, n):
    if sol[-1] < arr[i]:
        sol.append(arr[i])
    else:
        for j in range(len(sol)):
            if sol[j] >= arr[i]:
                sol[j] = arr[i]
                break

print(len(sol))

import bisect

x = int(input())
A = list(map(int, input().split()))

dp = [A[0]]

for i in range(1, x):
    if A[i] > dp[-1]:
        dp.append(A[i])
    else:
        idx = bisect.bisect_left(dp, A[i])
        dp[idx] = A[i]

print(len(dp))

