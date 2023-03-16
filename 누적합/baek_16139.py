# 2023/03/16 Baek 16139

import sys
input = sys.stdin.readline

S = input().strip()
len_S = len(S)

alpha_dict = {}
for i in range(26):
    alpha_dict[chr(97 + i)] = [0] * len_S

for i in range(len_S):
    alpha_dict[S[i]][i] = 1

for key in alpha_dict.keys():
    for i in range(1, len_S):
      alpha_dict[key][i] += alpha_dict[key][i - 1]

q = int(input())
for _ in range(q):
    a, l, r = input().strip().split()
    l = int(l)
    r = int(r)
    if l == 0:
        print(alpha_dict[a][r])
    else:
      print(alpha_dict[a][r] - alpha_dict[a][l - 1])