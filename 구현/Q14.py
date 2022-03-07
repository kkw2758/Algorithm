# 2020 KAKAO BLIND RECRUITMENT 외벽점검
from itertools import permutations

n = int(input())
weak = list(map(int, input().split()))
dist = list(map(int, input().split()))

def solution(n, weak, dist):
    answer = 0
    length = len(weak)
    for i in range(length):
        weak.append(n + weak[i])
    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start + 1, start + length):
                if weak[index] > position:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer

print(solution(n,weak,dist))