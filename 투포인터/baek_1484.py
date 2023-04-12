# 2023/04/12 Baek 1484

G = int(input())

result = []
start = 1
end = 2

while start != end:
    difference = end ** 2 - start ** 2
    if difference == G:
      result.append(end)
      start += 1
    elif difference < G:
       end += 1
    else:
       start += 1

if result:
   for i in result:
      print(i)
else:
   print(-1)