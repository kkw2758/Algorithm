# 2022/11/25 Baek 1477

import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
locations = list(map(int, input().split()))
locations.append(0)
locations.append(L)
locations.sort()

start = 1
end = L - 1

result = 0

while start <= end:
  mid = (start + end) // 2
  count = 0

  for i in range(1, len(locations)):
    count += (locations[i] - locations[i - 1] - 1) // mid

  if count > M:
    start = mid + 1
  else:
    end = mid - 1
    result = mid

print(result)

# import sys
# input = sys.stdin.readline

# N, M, L = map(int, input().split())
# locations = list(map(int, input().split()))
# locations.append(0)
# locations.append(L)
# locations.sort()

# start = 1
# end = L - 1

# result = 0

# while start <= end:
#   mid = (start + end) // 2
#   count = 0

#   for i in range(1, len(locations)):
#     if locations[i] - locations[i - 1] > mid:
#       count += (locations[i] - locations[i - 1] - 1) // mid

#   if count > M:
#     start = mid + 1
#   else:
#     end = mid - 1
#     result = mid

#   if count == M:
#     end = mid - 1
#     result = mid
#   elif count > M:
#     start = mid + 1
#   else:
#     end = mid - 1

# print(result)