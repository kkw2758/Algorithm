num_list = list(map(int, list(input())))
result = num_list[0]

for i in range(1, len(num_list)):
    if result == 0 or num_list[i] == 0 or num_list[i] == 1:
        result += num_list[i]
    else:
        result *= num_list[i]

print(result)
