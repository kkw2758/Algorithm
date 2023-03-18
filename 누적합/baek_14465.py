# 2023/03/18 Baek 14465

import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
traffic_lights = [1] * (N + 1)
traffic_lights[0] = 0

for _ in range(B):
    traffic_lights[int(input())] = 0

for i in range(1, N + 1):
   traffic_lights[i] += traffic_lights[i - 1]

broken_cnt = int(1e9)
for i in range(1, N - K + 1):
  broken_cnt = min(broken_cnt, K - (traffic_lights[i + K] - traffic_lights[i]))

print(broken_cnt)