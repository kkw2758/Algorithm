# 2022/09/01 Baek 11723
import sys
input = sys.stdin.readline
m = int(input())
S = set()
for _ in range(m):
  oper = list(input().rstrip().split())
  if oper[0] == "add":
    S.add(int(oper[1]))
  elif oper[0] == "remove":
    if int(oper[1]) in S:
      S.remove(int(oper[1]))
  elif oper[0] == "check":
    if int(oper[1]) in S:
      print(1)
    else:
      print(0)
  elif oper[0] == "toggle":
    if int(oper[1]) in S:
      S.remove(int(oper[1]))
    else:
      S.add(int(oper[1]))
  elif oper[0] == "all":
    S = set([i for i in range(1,21)])
  elif oper[0] == "empty":
    S = set()