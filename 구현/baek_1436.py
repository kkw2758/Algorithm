# 2023/02/02 Baek 1436

N = int(input())
number = 666
cnt = 0
while True:
    if "666" in str(number):
        cnt += 1
    if cnt == N:
        break
    number += 1

print(number)