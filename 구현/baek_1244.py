# 2023/06/13 Baek 1244

import sys
input = sys.stdin.readline

N = int(input())
status = [-1] + list(map(int, input().split()))
# 1 - ON
# 0 - OFF

students = int(input())
for _ in range(students):
    # 1 - man, 2 - woman
    gender, number = map(int, input().split())
    
    if gender == 1:
        cnt = 1
        while number * cnt <= N:
            if status[number * cnt] == 0:
                status[number * cnt] = 1
            else:
                status[number * cnt] = 0
            cnt += 1
    elif gender == 2:
        cnt = 1
        while number + cnt <= N and number - cnt >= 1:
            if status[number + cnt] != status[number - cnt]:
                break
            cnt += 1
        cnt -= 1
        for i in range(number - cnt , number + cnt + 1):
            if status[i] == 0:
                status[i] = 1
            else:
                status[i] = 0


for i in range(1, N + 1, 20):
    print(*status[i:i+20])