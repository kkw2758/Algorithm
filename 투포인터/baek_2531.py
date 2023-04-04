# 2023/04/04 Baek 2531

# 시간초과 풀이
# import sys
# input = sys.stdin.readline

# N, d, k, c = list(map(int, input().split()))

# numbers = []
# for _ in range(N):
#     numbers.append(int(input()))

# numbers += numbers[:-1]

# result = k
# for start in range(N):
#     temp = set([c])
#     for j in range(start, start + k):
#         temp.add(numbers[j])

#     result = max(result, len(temp))

# print(result)

# k크기의 구간에서 쿠폰에 있는 값이 있거나 중복되는값이 하나라도 있으면 반복을 고려 x
import sys
input = sys.stdin.readline

N, d, k, c = list(map(int, input().split()))

numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers += numbers[:-1]

result = len(set(numbers))

for start in range(N):
    temp = set(numbers[start:start + k] + [c])
    result = max(result, len(temp))
    # 최대 먹을 수 있는 초밥 수  k + 1
    if result == k + 1:
        break

print(result)
