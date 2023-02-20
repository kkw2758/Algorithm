# 2023/02/20 Baek 5800

K = int(input())
for i in range(K):
    scores = list(map(int, input().split()))
    scores = scores[1:]
    scores.sort(reverse=True)
    largest_gap = 0
    for j in range(1, len(scores)):
        largest_gap = max(largest_gap, scores[j - 1] - scores[j])
    print("Class {}".format(i + 1))
    print("Max {}, Min {}, Largest gap {}".format(scores[0], scores[-1],largest_gap))