# 2023/04/03 Baek 2577

mul = 1
for i in range(3):
    mul *= int(input())

mul = str(mul)

for i in range(10):
    print(mul.count(str(i)))