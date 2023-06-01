# 2023/06/01 Baek 10773

K = int(input())

numbers = []
for i in range(K):
    number = int(input())
    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)

print(sum(numbers))
