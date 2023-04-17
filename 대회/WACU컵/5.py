# 질량 / 부피 = 밀도
# 섞이기 전 밀도, 두 금속의 질량 비율

# d1, d2 밀도
# x = 질량의 비율

# m1, m2
# v1, v2
# (m1 + m2) / (v1 + v2) = result
# m1 / v1 = d1
# m2 / v2 = d2

# (m1 + m2) / (m1/d1 + m2/d2) = result


d1, d2, x = map(int, input().split())

first = x/100 / max(d1, d2)
second = (100 - x)/100 / min(d1, d2)
print(1/(first + second))