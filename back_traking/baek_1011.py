# 2023/03/04 Baek 1011

import sys
sys.setrecursionlimit(10**8)

def dfs(x, y, before, move_cnt):
    global result
    if x == y and before == 1:
        result = min(result, move_cnt)
        return
    if x >= y:
        return
    for move_disatnce in [before - 1, before, before + 1]:
        if move_disatnce > 0:
            dfs(x + move_disatnce, y, move_disatnce, move_cnt + 1)


T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    result = int(1e9)
    dfs(x, y, 0, 0)
    print(result)