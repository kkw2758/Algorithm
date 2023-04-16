# 2023/04/16 WACU컵 3번

N = int(input())
# 최소의 행동 횟수
# 생성하고 무조건 복제하자

cnt = 0
temp = 0
while temp < N:
    if temp == 0:
        cnt += 1
        temp = 1
        continue
    temp *= 2
    cnt += 1

print(cnt)