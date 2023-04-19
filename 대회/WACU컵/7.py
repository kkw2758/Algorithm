# # 2023/04/20 WACU컵 7번
# N, K = map(int, input().split())

# before = 1
# for i in range(2,N + 1):
#     before = (before * (10 ** i))%K
# print(before)

result = sorted(list(map(int, input().split())))
for i in result:
    print(i, end = " ")