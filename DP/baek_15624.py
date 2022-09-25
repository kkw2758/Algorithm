# 2022/09/25 Baek 15624

n = int(input())

before = 1
before_before = 0
for i in range(2, n + 1):
  before, before_before = (before + before_before) % 1000000007, before  % 1000000007

print(before)