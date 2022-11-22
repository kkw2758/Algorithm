# 2022/11/21 Baek 14921

# 투포인터 사용 풀이
import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
liquids = list(map(int, input().split()))

left = 0
right = N - 1

ans = INF
ans_left = 0
ans_right = N - 1

while left < right:
  sum = liquids[left] + liquids[right]

  if abs(ans) > abs(sum):
    ans_left = left
    ans_right = right
    ans = sum

  if sum == 0:
    break
  elif sum < 0:
    left += 1
  else:
    right -= 1

print(ans)

# 투포인터 이분 탐색
import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
liquids = list(map(int, input().split()))

ans = INF

for i in range(N - 1):
  current = i
  left = i + 1
  right = N - 1

  while left <= right:
    mid = (left + right) // 2
    sum = liquids[mid] + liquids[current]

    if abs(ans) > abs(sum):
      ans = sum

    if sum == 0:
      break
    if sum < 0:
      left = mid + 1
    else:
      right = mid - 1
  
print(ans)