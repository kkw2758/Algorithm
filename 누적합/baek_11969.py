# import sys
# input = sys.stdin.readline

# N, Q = map(int, input().split())
# numbers = []
# first = [0] * (N  + 1)
# second = [0] * (N  + 1)
# third = [0] * (N  + 1)

# for i in range(N):
#     number = int(input())
#     numbers.append(number)
#     if number == 1:
#         first[i + 1] += first[i] + 1
#         second[i + 1] = second[i]
#         third[i + 1] = third[i]
#     elif number == 2:
#         first[i + 1] += first[i]
#         second[i + 1] = second[i] + 1
#         third[i + 1] = third[i]
#     else:
#         first[i + 1] += first[i]
#         second[i + 1] = second[i]
#         third[i + 1] = third[i] + 1

# for _ in range(Q):
#     a, b = map(int, input().split())
#     print(first[b] - first[a - 1], second[b] - second[a - 1], third[b] - third[a - 1])



import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
numbers = []
temp = [[0,0,0] for _ in range(N + 1)]
for i in range(N):
    number = int(input())
    numbers.append(number)
    temp[i + 1][0] += temp[i][0]
    temp[i + 1][1] += temp[i][1]
    temp[i + 1][2] += temp[i][2]
    temp[i + 1][number - 1] += 1

for _ in range(Q):
    a, b = map(int, input().split())
    print(temp[b][0] - temp[a - 1][0], temp[b][1] - temp[a - 1][1], temp[b][2] - temp[a - 1][2])
