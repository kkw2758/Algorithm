# s = input()

# alpha_list = []
# sum = 0

# for x in s:
#     if 65 <= ord(x) <= 90:
#         alpha_list.append(x)
#     else:
#         sum += int(x)

# alpha_list.sort()
# result = "".join(alpha_list) + str(sum)
# print(result)

s = input()

result = []
sum = 0

for x in s:
    if x.isalpha():
        result.append(x)
    else:
        sum += int(x)

result.sort()
if sum != 0:
    result.append(str(sum))

print("".join(result))