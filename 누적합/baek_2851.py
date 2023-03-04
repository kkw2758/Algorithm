# 2023/03/04 Baek 2851

scores = [0]
result = 0

for i in range(10):
    scores.append(int(input()))

for i in range(1, 11):
    scores[i] = scores[i - 1] + scores[i]
    if abs(100 - scores[i]) <= abs(100 - result):
        result = scores[i]

print(result)