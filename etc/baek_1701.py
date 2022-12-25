# # 2022/12/21 Baek 1701

# def make_table(pattern):
#   pattern_size = len(pattern)
#   table = [0] * pattern_size
#   i = 0

#   for j in range(1, pattern_size):
#     while i > 0 and pattern[i] != pattern[j]:
#       i = table[i - 1]

#     if pattern[i] == pattern[j]:
#       i += 1
#       table[j] = i

#   return table

# def kmp(all_string, pattern):
#   table = make_table(pattern)
#   string_size = len(all_string)
#   pattern_size = len(pattern)
#   cnt = 0
#   i = 0
#   for j in range(string_size):
#     while i > 0 and pattern[i] != all_string[j]:
#       i = table[i - 1]

#     if pattern[i] == all_string[j]:
#       if i == pattern_size - 1:
#         i = table[i]
#         cnt += 1
#       else:
#         i += 1

#   return cnt

# target_string = input()
# result = 0
# result_pattern = ""
# pattern_check = set()
# for pattern_len in range(1, len(target_string) + 1):
#   for start in range(len(target_string) - pattern_len):
#     pattern = target_string[start:start + pattern_len]
#     if pattern not in pattern_check:
#       pattern_check.add(pattern)
#       kmp_result = kmp(target_string, pattern)
#       if kmp_result >= 2:
#         result = max(result, len(pattern))

# print(result)

def make_table(pattern):
  pattern_size = len(pattern)
  table = [0] * pattern_size
  i = 0

  for j in range(1, pattern_size):
    while i > 0 and pattern[i] != pattern[j]:
      i = table[i - 1]

    if pattern[i] == pattern[j]:
      i += 1
      table[j] = i

  return max(table)

target_string = input()
result = 0
for idx in range(len(target_string)):
    result = max(result, make_table(target_string[idx:]))

print(result)