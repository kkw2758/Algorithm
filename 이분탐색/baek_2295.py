# 2022/11/19 Baek 2295

# from itertools import combinations

# N = int(input())
# numbers = []
# numbers.sort()

# for _ in range(N):
#   numbers.append(int(input()))

# def binary_search(start, end, target):
#   while start <= end:
#     mid = (start + end) // 2
#     if numbers[mid] == target:
#       return mid
#     elif numbers[mid] > target:
#       end = mid - 1
#     else:
#       start = mid + 1

#   return -1

# candidates = list(combinations(numbers, 3))
# result = 0

# for candidate in candidates:
#   target = sum(candidate)
#   if target > numbers[0]:
#     break
#   result = max(result, binary_search(0, N - 1, target))

# print(numbers[result])

# 2022/11/19 Baek 2295
# https://konghana01.tistory.com/299?category=958095 참고
# 접근 방법
# x + y = k - z 를 이용해 x + y의 배열을 정렬한 뒤, k와 z의 이중반복문을 통해
# x + y 배열을 이진 탐색으로 탐색한 뒤, 가장 큰 값을 출력한다.

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
arr2 = []
for x in range(n):
  for y in range(x, n):
    arr2.append(arr[x] + arr[y])

arr2.sort()
result = 0
for z in range(n):
  for k in range(z, n):
    a = arr[k] - arr[z]
    start = 0
    end = len(arr2) - 1
    while start <= end:
      mid = (start + end) // 2
      b = arr2[mid]
      if a > b:
        start = mid + 1
      elif a < b:
        end = mid - 1
      else:
        result = max(result, arr[k])
        break

print(result)


# 이진 탐색을 이용하지 않고 x + y = k - z 를 이용한 풀이
n = int(input())

u = set()
for i in range(n):
    u.add(int(input()))

a_b_sums = set()
for i in u:
    for j in u:
        a_b_sums.add(i + j)

ans = []
for i in u:
    for j in u:
        if (i - j) in a_b_sums:
            ans.append(i)

ans.sort(reverse=True)
print(ans[0])