# # 2023/04/05 Baek 7795

# # 2중 for문
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     A.sort()
#     B.sort()
    
#     result = 0
#     for A_idx in range(N):
#         for B_idx in range(M):
#             if A[A_idx] > B[B_idx]:
#                 result += 1
#                 continue
#             break
              
#     print(result)


# # lower_bound
# import sys
# from bisect import bisect_left

# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     A.sort()
#     B.sort()

#     result = 0
#     for i in range(N):
#         result += bisect_left(B, A[i])

#     print(result)


# 투 포인터
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     A.sort(reverse=True) # 내림차순
#     B.sort()
#     # 8 7 3 1 1 
#     # 1 3 6
#     result = 0
#     end = M - 1
#     for i in range(N):
#         while end >= 0:
#             if A[i] > B[end]:
#                 result += end + 1
#                 break
#             else:
#                 end -= 1

#     print(result)

# 투 포인터
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     A.sort(reverse=True)# 내림차순
#     B.sort(reverse=True)
#     # 8 7 3 1 1
#     # 1 3 6
#     result = 0
#     start = 0
#     for i in range(N):
#         while start < M:
#             if A[i] > B[start]:
#                 result += M - start
#                 break
#             else:
#                 start += 1

#     print(result)



import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    # 1 1 3 7 8
    # 1 3 6
    result = 0
    start = 0
    for i in range(N):
        while start < M:
            if A[i] <= B[start]:
                break
            else: # A[i] > B[start]
                start += 1
        result += start
    print(result)