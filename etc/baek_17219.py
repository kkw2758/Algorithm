# 2022/09/03 Baek 17219

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
ad_pw = {}
for _ in range(N):
  ad, pw = input().rstrip().split()
  ad_pw[ad] = pw
for _ in range(M):
  ad = input().rstrip()
  print(ad_pw[ad])