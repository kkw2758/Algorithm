# 2023/03/29 Baek 1451

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [[0] * (M + 1)]

for _ in range(N):
    numbers.append([0] + list(map(int, list(input().strip()))))

# 2차원 배열에서의 누적합 구하기
for i in range(1, N + 1):
    for j in range(1, M + 1):
        numbers[i][j] += numbers[i - 1][j] + numbers[i][j - 1] - numbers[i - 1][j - 1]

result = 0
# case 1
for i in range(1, M - 1):
    for j in range(i + 1, M):
        result = max(result, numbers[N][i] * (numbers[N][j] - numbers[N][i]) * (numbers[N][M] - numbers[N][j]))

# case 2
for i in range(1, N - 1):
    for j in range(i + 1, N):
        result = max(result, numbers[i][M] * (numbers[j][M] - numbers[i][M]) * (numbers[N][M] - numbers[j][M]))

# case 3
for i in range(1, N):
    for j in range(1, M):
        result = max(result, numbers[N][j] * (numbers[i][M] - numbers[i][j]) * (numbers[N][M] - numbers[N][j] - (numbers[i][M] - numbers[i][j])))

# case 4
for i in range(1, N):
    for j in range(1, M):
        result = max(result, numbers[i][j] * (numbers[N][j] - numbers[i][j]) * (numbers[N][M] - numbers[N][j]))

# case 5
for i in range(1, N):
    for j in range(1, M):
        result = max(result, numbers[i][j] * (numbers[i][M] - numbers[i][j]) * (numbers[N][M] - numbers[i][M]))

# case 6
for i in range(1, N):
    for j in range(1, M):
        result = max(result, numbers[i][M] * (numbers[N][j] - numbers[i][j]) * (numbers[N][M] - numbers[i][M] - (numbers[N][j] - numbers[i][j])))

print(result)