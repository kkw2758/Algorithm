# 2022/11/24 Baek 2473

import sys
input = sys.stdin.readline

INF = sys.maxsize
N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

ans = INF
ans_current = 0
ans_left = 0
ans_right = N - 1

for i in range(N):
    current = liquids[i]
    tmp = liquids[:i] + liquids[i + 1:]
    start = 0
    end = N - 2

    while start < end:
        target = current + tmp[start] + tmp[end]
        if ans > abs(target):
            ans = abs(target)
            ans_current = current
            ans_left = tmp[start]
            ans_right = tmp[end]

        if target == 0:
            break

        elif target > 0:
            end -= 1
        else:   # target < 0
            start += 1

result = [ans_left, ans_current, ans_right]
result.sort()
for i in result:
    print(i, end = " ")



import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

ans = sys.maxsize

for i in range(N - 2):
    start = i + 1
    end = N - 1
    while start < end:
        tmp = liquids[i] + liquids[start] + liquids[end]
        if ans > abs(tmp):
            ans = abs(tmp)
            result = [liquids[i], liquids[start], liquids[end]]
        if tmp > 0:
            end -= 1
        elif tmp < 0:
            start += 1
        else:
            break

print(result[0], result[1], result[2])