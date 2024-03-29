# 2023/05/06 Baek 2738

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]
matrix2 = [list(map(int, input().split())) for _ in range(N)]

result_matrix = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        result_matrix[i][j] += (matrix1[i][j] + matrix2[i][j])
        
for i in result_matrix:
    print(*i)