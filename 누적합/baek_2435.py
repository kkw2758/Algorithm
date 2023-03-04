# 2023/03/04 Baek 2435

N, K = map(int, input().split())
temperatures = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    temperatures[i] += temperatures[i - 1]

result = -(int(1e90))
for i in range(K, N + 1):
    result = max(result, temperatures[i] - temperatures[i - K])

print(result)