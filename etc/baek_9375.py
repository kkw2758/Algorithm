# 2022/09/03 Baek 9375

# 처음에  combinations모듈로 풀려고했지만 시간초과 
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  cloth_dic = {}
  for _ in range(n):
    name, type = input().split()
    if type in cloth_dic:
      cloth_dic[type].append(name)
    else:
      cloth_dic[type] = [name]

  count = 1
  for key in cloth_dic.keys():
      count *= len(cloth_dic[key]) + 1
  print(count-1)

import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  clothes = []
  for _ in range(n):
    type = input().split()[1]
    clothes.append(type)

  clothes_Counter = Counter(clothes)

  count = 1
  for key in clothes_Counter.keys():
      count *= clothes_Counter[key] + 1
  print(count - 1)  