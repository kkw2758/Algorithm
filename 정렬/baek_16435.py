# 2023/02/22 Baek 16435

N, L = map(int, input().split())
integers = list(map(int, input().split()))

integers.sort()
for i in integers:
    if i <= L:
        L += 1

print(L)