# # 2022/09/09 Baek 11286

# import heapq

# N = int(input())

# plus_hip = []
# minus_hip = []
# for _ in range(N):
#   x = int(input())
#   if x == 0:
#     if len(plus_hip) == 0 and len(minus_hip) == 0:
#       print(0)
#     elif len(plus_hip) == 0:
#       print(-heapq.heappop(minus_hip))
#     elif len(minus_hip) == 0:
#       print(heapq.heappop(plus_hip))
#     else:
#       if abs(plus_hip[0]) < abs(minus_hip[0]):
#         print(heapq.heappop(plus_hip))
#       else:
#         print(-heapq.heappop(minus_hip))
#   else:
#     if x > 0:
#       heapq.heappush(plus_hip, x)
#     else:
#       heapq.heappush(minus_hip, -x)



# 2022/09/09 Baek 11286

import heapq

N = int(input())

q = []
for _ in range(N):
  x = int(input())
  if x == 0:
    if len(q) == 0:
      print(0)
    else:
      value, flag = heapq.heappop(q)
      print(value * flag)
  else:
    flag = 1
    if x < 0:
      flag = -1
    heapq.heappush(q, (x * flag, flag))