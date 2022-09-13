# 2022/09/13 Baek 2407

import math

n, m = map(int, input().split())
bunza = math.factorial(n)
bunmo = (math.factorial(n - m)) * (math.factorial(m))
print(bunza // bunmo)