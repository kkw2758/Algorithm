# 2021/06/21 Baek 12015


import sys
read = sys.stdin.readline

# 이진탐색 기반 lower_bound
# 정렬된 리스트에서 value 값보다 처음으로 크거나 같은값이 나오는 인덱스를 찾는다. (리스트 값이 중복되더라도 사용가능)
# ex [1,2,2,2,4] value = 2 -> return 1
def lower_bound(array, start, end, value):
    while start < end:
        mid = (start + end) // 2
        
        if array[mid] < value:
            start = mid + 1
        else:
            end = mid

    return start

# 내가 처음으로 구현한 코드 
dp = [0]
n = int(read())
array = list(map(int, read().strip().split()))

for i in range(len(array)):
    idx = lower_bound(dp, 0, len(dp), array[i])
    if idx == len(dp):
        dp.append(array[i])
    else:       
        if dp[idx] > array[i]:
            dp[idx] = array[i]

print(len(dp) - 1)

# 인터넷 참고 풀이
dp = [0]
n = int(read())
array = list(map(int, read().strip().split()))

for i in range(len(array)):
    if dp[-1] < array[i]:
        dp.append(array[i])
    else:
        idx = lower_bound(dp, 0, len(dp), array[i])
        dp[idx] = array[i]

print(len(dp) - 1)



import sys
from bisect import bisect_left
read = sys.stdin.readline

dp = [0]
n = int(read())
array = list(map(int, read().strip().split()))

for i in range(len(array)):
    if dp[-1] < array[i]:
        dp.append(array[i])
    else:
        idx = bisect_left(dp,array[i])
        dp[idx] = array[i]

print(len(dp) - 1)