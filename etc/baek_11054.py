# 2023/05/01 Baek 11054

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

# 1 5 2 1 4 3 4 5 2 1
# 1   2     3 4 5 2 1

# 1 <= N <= 1000

# 입력으로 받은 리스트가 정렬되어 있지 않으므로 이분탐색, lower_bound 사용불가
# 완전탐색? N이 1000이므로 가능할 것 같다.

# 증가하는 부분 수열

import bisect

def bitonic(li):
    n = len(li)
    dp = [li[0]]
    for i in range(1, n):
        if li[i] > li[-1]:
            continue
        if li[i] > dp[-1]:
            dp.append(li[i])
        else:
            index = bisect.bisect_left(dp, li[i])
            dp[index] = li[i]
            
    return len(dp)

result = 0
for i in range(N):
    # print("numbers[:i + 1] : ", numbers[:i + 1], bitonic(numbers[:i + 1]))
    # print("numbers[i::-1] : ", numbers[i:][::-1], bitonic(numbers[i:][::-1]))
    result = max(result, bitonic(numbers[:i + 1]) + bitonic(numbers[i:][::-1]) - 1)
    
print(result)

# 참고 풀이 1
# https://seohyun0120.tistory.com/entry/%EB%B0%B1%EC%A4%80-11054-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4

x = int(input())

case = list(map(int, input().split()))  # 1 5 2 1 4 3 4 5 2 1
reverse_case = case[::-1]               # 1 2 5 4 3 4 1 2 5 1

increase = [1 for i in range(x)]
decrease = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
            
result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease[x - i - 1] - 1

print(max(result))

# 참고 풀이 2
x = int(input())

case = list(map(int, input().split()))

increase = [1 for i in range(x)]
for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j] + 1)

decrease = [1 for i in range(x)]
for i in range(x - 1, -1, -1):
    for j in range(x - 1, i, -1):
        if case[i] > case[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
            
result = [0 for _ in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease[i] - 1
    
print(max(result))