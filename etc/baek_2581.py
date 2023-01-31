# 2023/01/31 Baek 2581

M = int(input())
N = int(input())

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


cnt = 0
min_value = 10000
for i in range(M, N + 1):
    if is_prime(i):
        cnt += i
        min_value = min(min_value, i)

if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(min_value)