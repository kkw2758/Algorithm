# 2022/09/11 Baek 5430

import sys

input = sys.stdin.readline

def func(): 
  p = input().rstrip()
  n = int(input())
  ary = input().rstrip()[1:-1]
  if not ary:
    ary = []
  else:
    ary = ary.split(",")
  
  R_count = 0
  for flag in p:
    if flag == "R":
      R_count += 1
    elif flag == "D":
      idx = 0
      if R_count % 2 == 1:
        idx = -1
      if not ary:
        return "error"
      ary.pop(idx)

  if R_count % 2 == 1:
    ary.reverse()
  result = "["
  result += ",".join(ary)
  result += "]"
  return result

T = int(input())
for _ in range(T):
  print(func())

import sys
from collections import deque

input = sys.stdin.readline

def func(): 
  p = input().rstrip()
  n = int(input())
  ary = input().rstrip()[1:-1]
  if not ary:
    ary = []
  else:
    ary = ary.split(",")
  
  ary = deque(ary)
  
  R_count = 0
  for flag in p:
    if flag == "R":
      R_count += 1
    elif flag == "D":
      if not ary:
        return "error"
        
      if R_count % 2 == 1:
        ary.pop()
      else:
        ary.popleft()

  if R_count % 2 == 1:
    ary.reverse()
  result = "["
  result += ",".join(ary)
  result += "]"
  return result


T = int(input())
for _ in range(T):
  print(func())