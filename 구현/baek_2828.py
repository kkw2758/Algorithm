# 2023/02/28 Baek 2828

N, M = map(int, input().split())
j = int(input())
head = 1
cnt = 0
for i in range(j):
    position = int(input())

    if position < head:
        cnt += head - position
        head = position
    elif position > head + M - 1:
        cnt += position - (head + M - 1)
        head = position - M + 1
    print(i, cnt)
print(cnt)