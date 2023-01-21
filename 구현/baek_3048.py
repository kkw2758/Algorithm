# 2023/01/22 Baek 3048

N1, N2 = map(int, input().split())

direction_info_dic = {}

group = list(input())
reverse_group = list(input())

for i in group:
  direction_info_dic[i] = 1

for i in reverse_group:
  direction_info_dic[i] = -1

group.reverse()
order_list = group + reverse_group
N = len(order_list)

T = int(input())
for i in range(T):
  jump_index = []
  for j in range(N):
    d = direction_info_dic[order_list[j]]
    if 0 <= j + d < N:
      if direction_info_dic[order_list[j + d]] != d:
        target = [j, j + d]
        target.sort()
        if target not in jump_index:
          jump_index.append(target)


  for x, y in jump_index:
    order_list[x], order_list[y] = order_list[y], order_list[x]

print("".join(order_list))