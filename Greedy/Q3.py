# 2022-01-11 baek 1439

num_str = input()
result = 0

for i in range(len(num_str) - 1):
    if num_str[i] != num_str[i + 1]:
        result += 1

if result % 2 == 1:
    result = result//2 + 1
else:
    result = result//2

print(result)