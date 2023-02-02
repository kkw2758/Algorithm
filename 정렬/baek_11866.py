# 2023/02/02 Baek 11866

N, K = map(int, input().split())

ary = [i for i in range(1, N + 1)]
result = []
idx = 0
for _ in range(N):
    idx = (idx + (K - 1)) % len(ary)
    result.append(str(ary.pop(idx)))

print("<" + ", ".join(result) + ">")