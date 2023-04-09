# 2023/04/10 Baek 2436

# g = 최대공약수
# l = 최소공배수
# l = a x b x g
# a * b = l / g
import math
g, l = list(map(int, input().split()))

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

result = 200000000
divide = l // g
answer = ""
for a in range(1, int(math.sqrt(divide)) + 1):
    b = divide//a
    if divide % a == 0 and gcd(a, b) == 1:
        if a*g+ b*g < result:
            answer = "{} {}".format(a*g, b*g)

print(answer)