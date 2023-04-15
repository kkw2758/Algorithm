# 2023/04/12 Baek 4158

while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    A = []
    for i in range(N):
        A.append(int(input()))
    B = []
    for i in range(M):
        B.append(int(input()))

    B_idx = 0
    result = 0
    for A_idx in range(N):
        while B_idx < M:
            if A[A_idx] == B[B_idx]:
                result += 1
                B_idx += 1
                break
            elif A[A_idx] > B[B_idx]:
                B_idx += 1
            else:
                break
    print(result)

from bisect import bisect_left
while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    A = []
    for i in range(N):
        A.append(int(input()))
    B = []
    for i in range(M):
        B.append(int(input()))

    result = 0
    for A_idx in range(N):
        lower_bound_idx = bisect_left(B, A[A_idx])
        if A[A_idx] == B[lower_bound_idx]:
            result += 1
    
    print(result)

from collections import defaultdict

while True:
    int_dict = defaultdict(int)
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    result = 0

    A = []
    for i in range(N):
        int_dict[int(input())] += 1

    B = []
    for i in range(M):
        if int_dict[int(input())] == 1:
            result += 1
    
    print(result)