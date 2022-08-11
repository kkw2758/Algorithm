# from itertools import permutations

# n = int(input())
# array_a = list(map(int, input().split()))
# count = list(map(int, input().split()))
# temp = ["+", "-", "*", "//"]

# operator_list = []
# for idx in range(len(count)):
#     for _ in range(count[idx]):
#         operator_list.append(temp[idx])

# candidates = list(set(permutations(operator_list, len(operator_list))))

# min_value = 1e9
# max_value = -1e9

# for candidate in candidates:
#     now = array_a[0]
#     for idx in range(1, len(array_a)):
#         operator = candidate[idx - 1]
#         if operator == "+":
#             now += array_a[idx]
#         elif operator == "-":
#             now -= array_a[idx]
#         elif operator == "*":
#             now *= array_a[idx]
#         else:
#             if now < 0:
#                 now = -(-now // array_a[idx])
#             else:
#                 now //= array_a[idx]

#     min_value = min(min_value, now)
#     max_value = max(max_value, now)

# print(max_value)
# print(min_value)

# n = int(input())
# data = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())

# max_value = -1e9
# min_value = 1e9

# def dfs(i, now):
#     global min_value, max_value, add, sub, mul, div
#     print(now)
#     if i == n:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         if add > 0:
#             add -= 1
#             dfs(i + 1, now + data[i])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i + 1, now - data[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i + 1, now * data[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i + 1, int(now / data[i]))
#             div += 1

# dfs(1, data[0])

# print(max_value)
# print(min_value)

from itertools import product
from itertools import permutations

N = int(input())
array = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

operators = []
operators += [ "+" for _ in range(add)]
operators += [ "-" for _ in range(sub)]
operators += [ "*" for _ in range(mul)]
operators += [ "/" for _ in range(div)]

# candidates = product(operators, repeat = N-1)
candidates = list(set(permutations(operators)))

for candidate in candidates:
    now = array[0]
    for i in range(1, N):
        if candidate[i - 1] == "+":
            now += array[i]
        elif candidate[i - 1] == "-":
            now -= array[i]
        elif candidate[i - 1] == "*":
            now *= array[i]
        elif candidate[i - 1] == "/":
            now = int(now / array[i])

    max_value = max(max_value, now)
    min_value = min(min_value, now)
    
print(max_value)
print(min_value)