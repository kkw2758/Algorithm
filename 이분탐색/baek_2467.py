# 2022/11/19 Baek 2467
#이분 탐색
import sys
input = sys.stdin.readline

INF = int(10e9)
N = int(input())
liquids = list(map(int, input().split()))
ans = INF

for i in range(N - 1):
  current = liquids[i]

  start = i + 1
  end = N - 1

  while start <= end:
    mid = (start + end) // 2
    tmp = current + liquids[mid]

    if abs(tmp) < ans:
      ans = abs(tmp)
      ans_left = i
      ans_right = mid

    if tmp == 0:
      break
    if tmp < 0:
      start = mid + 1
    else:
      end = mid - 1

print(liquids[ans_left], liquids[ans_right])
  


# 2022/11/19 Baek 2467
#이분 탐색
import sys
INF = int(10e9)
N = int(input())
numbers = list(map(int, input().split()))

def parametric(first, start, end):
  before = (INF, 0, 0)
  while start <= end:
    mid = (start + end) // 2
    second = numbers[mid]
    value = first + second

    if value == 0:
      return 0, first, -first
    elif value > 0:
      end = mid - 1
    else:
      start = mid + 1

    if before[0] > abs(first + second):
      before = (abs(first + second), first, second)

  return before

result = []
for i in range(N - 1):
  first = numbers.pop(0)
  value, first, second = parametric(first, 0, len(numbers) - 1)
  result.append((value, first, second))


result.sort()
print(result[0][1], result[0][2])

# 투포인터 사용
import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

left_idx = 0
right_idx = n - 1

ans = abs(liquids[left_idx] + liquids[right_idx])
ans_left = left_idx
ans_right = right_idx

while left_idx < right_idx:
  tmp = liquids[left_idx] + liquids[right_idx]

  if abs(tmp) < ans:
    ans_left = left_idx
    ans_right = right_idx
    ans = abs(tmp)

    if ans == 0:
      break

  if tmp < 0:
    left_idx += 1
  else:
    right_idx -= 1

print(liquids[ans_left], liquids[ans_right])