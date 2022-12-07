# 2022/12/08 Baek 7785

n = int(input())
in_company = dict()
for _ in range(n):
  name, flag = input().split()
  if flag == "enter":
    in_company[name] = True
  elif flag == "leave":
    del(in_company[name])

in_company = sorted(list(in_company), reverse=True)
for name in in_company:
  print(name)