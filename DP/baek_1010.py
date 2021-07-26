# 2021/06/25 Baek 1010

# 문제에서 서쪽에서 동쪽으로 다리를 짓는데 다리가 겹치면 안되는 조건에 의해서 동쪽의 다리 개수 m개 중에서 서쪽의 다리 개수 n개 만큼의 사이클을 "순서상관없이" 뽑으면 된다고 판단!
# 문제를봤을때 알고리즘 분류를 보고 "dp로도 해결할 수 있구나"라고 생각을 했지만 방법이 생각이 나지않고 학교다닐때배운 조합공식만 계속 생각이났다..

# dp를 이용한 풀이
import sys

read = sys.stdin.readline

t = int(read())

dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

for i in range(t):
    n, m = map(int, read().split())
    print(dp[n][m])

# 조합 공식을 이용한 풀이
# 조합 공식 -> nCr 즉, n개에서 r개를 순서상관없이 뽑는경우  n! / r!(n-r)!

import sys
read = sys.stdin.readline

t = int(read())