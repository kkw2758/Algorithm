# 2023 01/29 Baek 1181

import sys
input = sys.stdin.readline

N = int(input())
word_list = [[] for _ in range(51)]

for _ in range(N):
  word = input().strip()
  if word not in word_list[len(word)]:
    word_list[len(word)].append(word)

for i in range(1, 51):
  if word_list[i] != []:
    word_list[i].sort()
    for word in word_list[i]:
      print(word)
    