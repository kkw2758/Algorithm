# 2023/05/29 Baek 10866

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    flag = list(input().strip().split())
    if flag[0] == "push_front":
        q.appendleft(int(flag[1]))
    elif flag[0] == "push_back":
        q.append(int(flag[1]))
    elif flag[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif flag[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif flag[0] == "size":
        print(len(q))
    elif flag[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif flag[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif flag[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)