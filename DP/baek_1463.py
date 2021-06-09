# 2021/06/09 Baek 1463


#바텀업 방식
n = int(input())

dp = [0] * (n + 1)


def baek_1463(n):
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + 1
        
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)           
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

baek_1463(n)
print(dp[n])

#탑다운 방식
def top_down(n):
    if n in memo:
        return memo[n]

    m = 1 + min(top_down(n//2) + n % 2, top_down(n//3) + n % 3)
    memo[n] = m
    return memo[n]

memo = {1:0, 2: 1}
n = int(input())
print(top_down(n))


# 집합을 이용한 풀이 신기해서 넣어봄
# c의 인덱스 값이 연산한 횟수를 나타내는데 처음으로 1이나오게되는 인덱스가 n을 1로만드는 최소한의 연산횟수를 나타냄.
a=int(input())
c=[{a}]
n=0
while 1 not in c[n]:
    d=set()
    for i in c[n]:
        if i%3==0:
            d.add(i//3)
        if i%2==0:
            d.add(i//2)
        d.add(i-1)
    #d -= c[n]
    c.append(d)
    print(c)
    n+=1
print(n)