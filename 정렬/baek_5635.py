# 2023/02/19 Baek 5635

N = int(input())
birthday_info = []
for _ in range(N):
  name, d, m, y = input().split()
  birthday_info.append((name, int(d), int(m), int(y)))

birthday_info.sort(reverse=True, key= lambda x:(x[3],x[2],x[1]))
print(birthday_info[0][0])
print(birthday_info[-1][0])