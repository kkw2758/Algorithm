# 2023/06/05 Baek 1966

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    q = deque()
    for i in range(len(numbers)):
        q.append((numbers[i], i))

    idx = 1
    while q:
        max_value = max(q)[0]
        value, position = q.popleft()
        if value == max_value:
            if position == M:
                print(idx)
                break
            else:
                idx += 1
        else:
            q.append((value, position))


    
   
