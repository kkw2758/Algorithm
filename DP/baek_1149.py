# 2021/06/10 Baek 1149
import sys

# n = int(input())
n = int(sys.stdin.readline())

color_cost_list = [[0,0,0]]
for _ in range(n):
    #color_cost_list.append(list(map(int,input().split())))
    color_cost_list.append(list(map(int, sys.stdin.readline().split())))
dp = [[-1, -1, -1] for _ in range(n + 1)]

dp[1][0] = color_cost_list[1][0]
dp[1][1] = color_cost_list[1][1]
dp[1][2] = color_cost_list[1][2]

#print("dp =",dp)
#print("color_cost_list =",color_cost_list)

for i in range(2, n + 1):
    for now_color_idx in range(3):    # 0 = R, 1 = G, 2 = B
        for before_color_idx in range(3):
            if now_color_idx == before_color_idx:
                continue
            if dp[i][now_color_idx] == -1:
                dp[i][now_color_idx] = dp[i-1][before_color_idx] + color_cost_list[i][now_color_idx]
                continue
            dp[i][now_color_idx] = min(dp[i][now_color_idx], dp[i-1][before_color_idx] + color_cost_list[i][now_color_idx])


print(min(dp[n][0], dp[n][1], dp[n][2]))