# 2023/01/27 Baek 1193

N = int(input())

cnt = 1

while True:
    if N - cnt <= 0:
        break
    N -= cnt
    cnt += 1

print(N)
print(cnt)

result = str(1 + N - 1) + "/" + str(cnt + 1 - N)
print(result)