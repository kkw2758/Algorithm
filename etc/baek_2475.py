import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
temp = 0
for number in numbers:
    temp += number ** 2
print(temp % 10)