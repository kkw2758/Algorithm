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

# 구하려고 하는 값 -휴게소들 사이의 거리의 최대값 중 최솟값
# count가 M보다 작은 경우에도 남는 휴게소들(count - M개)은
# 거리가 최대가 아닌 다른 곳에 아무렇게나 넣어도 최대값  mid는 유지 될 수 있음

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