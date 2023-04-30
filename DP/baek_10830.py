# 2023/04/30 Baek 10830

N, B = map(int, input().split())

# B의 범위가 엄청나게 크다 -> 그냥 정직하게 B만큼 A를 곱하면 무조건 시간초과

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    for i in range(N):
        row[i] = row[i] % 1000
    matrix.append(row)

# N의 범위가 2 <= N <= 5 이므로 상수 취급
def matrix_mul(matrix1, matrix2):
    n = len(matrix)
    result_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result = 0
            for k in range(n):
                    result += matrix1[i][k] * matrix2[k][j]

            result_matrix[i][j] = result % 1000

    return result_matrix


# 이전에 곱결과를 계속 이용할 수 없을까?
# dp 생각
# x ^^ B = ((x ^^ (B//2)) ^^ 2) * x ^^ (B%2)
# A ^^ 3 = ((A ^^ 1) ^^ 2) * A ^^ 1
# A ^^ 5 = ((A ^^ 2) ^^ 2) * A ^^ 1

dp = dict()
def func(cnt):
    if cnt in dp:
        return dp[cnt]
    if cnt == 1:
        dp[1] = matrix
        return dp[cnt]
     
    if cnt % 2 == 0:
        dp[cnt] = matrix_mul(func(cnt // 2), func(cnt // 2))
    else:
        dp[cnt] = matrix_mul(matrix_mul(func(cnt // 2), func(cnt // 2)), func(cnt % 2))

    return dp[cnt]
    

result = func(B)
for i in range(N):
    for j in range(N):
        print(result[i][j], end = " ")
    print()