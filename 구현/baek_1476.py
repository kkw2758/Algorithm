# 2023/02/02 Baek 1476

E, S, M = map(int, input().split())
e = 1
s = 1
m = 1

year = 1
while True:
    if (E, S, M) == (e, s, m):
        break
    e = e % 15 + 1 
    s = s % 28 + 1
    m = m % 19 + 1
    year += 1


print(year)