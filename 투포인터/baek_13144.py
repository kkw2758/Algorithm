# 2023/04/24 Baek 13144

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

# 길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때
# 같은 수가 여러 번 등장하지 않은 경우의 수를 구하는 프로그램을 작성하여라.

result = 0

# 연속해서 뽑기 때문에 정렬을하면 안될 것 같음
# 정렬하면 연속으로 뽑는 의미가 없으니까

start = 0
end = 0
temp = set()
while True:
    if numbers[end] not in temp:
        temp.add(numbers[end])
        end += 1
        if end >= N:
            end = N - 1
    else:
        result += len(temp)
        temp.remove(numbers[start])
        start += 1
        if start >= N:
            break

print(result)