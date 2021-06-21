# 2021/06/21 Baek 2748

def baek_2748(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        a,b = b, a + b

    return b

n = int(input())
print(baek_2748(n))