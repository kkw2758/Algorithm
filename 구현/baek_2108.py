# 2023/05/09 Baek 2108

import sys
from collections import defaultdict
N = int(input())
numbers = []
int_dict = defaultdict(int)
for i in range(N):
    number = int(input())
    int_dict[number] += 1
    numbers.append(number)
    
numbers.sort()

# 1. 산술평균
print(round(sum(numbers) / N))
# 2. 중앙값
print(numbers[N//2])
# 3. 최빈값
max_frequency_value = 0
temp_list = []
for key in list(int_dict.keys()):
    if int_dict[key] > max_frequency_value:
        max_frequency_value = int_dict[key]
        temp_list = [key]
    elif int_dict[key] == max_frequency_value:
        temp_list.append(key)
    
temp_list.sort()
if len(temp_list) == 1:
    print(temp_list[0])
else:
    print(temp_list[1])
    
# 4. 범위
print(numbers[-1] - numbers[0])