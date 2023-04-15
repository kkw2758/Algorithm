# 2023/04/15 Baek 2230
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

numbers.sort() # 투포인터를 적용하기위해서 정렬

start = 0
end = 0

result = int(10e9)
while start <= end and end < N:
    if numbers[end] - numbers[start] < M:
        end += 1
    else:
        result = min(result, numbers[end] - numbers[start])
        start += 1

print(result)

