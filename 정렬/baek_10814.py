# 2023/02/01 Baek 10814

import sys
input = sys.stdin.readline

N = int(input())

members = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    members.append((age, name, i))

members.sort(key=lambda x: (x[0], x[2]))

for member in members:
    print(member[0], member[1])