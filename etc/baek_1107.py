# 2022/09/02 Baek 1107

from itertools import product

INF = int(1e9)
N = int(input())
M = int(input())
buttons = set(([i for i in range(10)]))

if M != 0:
  broken_buttons = set(map(int, input().rstrip().split()))
  buttons = buttons - broken_buttons

buttons = list(map(str, list(buttons)))
length = len(str(N))

min_difference = INF
result1 = 0
for i in range(length - 1, length + 2):
  for candidate in product(buttons, repeat=i):
    temp = ""
    for string in candidate:
      temp += string
    if temp:
      temp = int(temp)
      if abs(temp - N) < min_difference:
        min_difference = abs(temp - N)
        result1 = temp

if N >= 100:
  result2 = N - 100
else:
  result2 = 100 - N

if len(buttons) == 0:
  result1 = INF
else:
  result1 = len(str(result1)) + abs(N - result1)
  # result1 = len(str(result1)) + min_difference

if result1 > result2:
  print(result2)
else:
  print(result1)

#참고 풀잉
#https://seongonion.tistory.com/99
import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)