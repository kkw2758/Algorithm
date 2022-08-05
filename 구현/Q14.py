# 2020 KAKAO BLIND RECRUITMENT 외벽점검
# from itertools import permutations

# n = int(input())
# weak = list(map(int, input().split()))
# dist = list(map(int, input().split()))

# def solution(n, weak, dist):
#     answer = 0
#     length = len(weak)
#     for i in range(length):
#         weak.append(n + weak[i])
#     answer = len(dist) + 1

#     for start in range(length):
#         for friends in list(permutations(dist, len(dist))):
#             count = 1
#             position = weak[start] + friends[count - 1]
#             for index in range(start, start + length):
#                 if weak[index] > position:
#                     count += 1
#                     if count > len(dist):
#                         break
#                     position = weak[index] + friends[count - 1]
#             answer = min(answer, count)

#     if answer > len(dist):
#         return -1
#     return answer

# print(solution(n,weak,dist))

# from itertools import permutations
# def solution(n, weak, dist):
#     L = len(weak)
#     cand = []
#     weak_point = weak + [w + n for w in weak]

#     for i, start in enumerate(weak):
#         for friends in permutations(dist):
#             count = 1
#             position = start
#             for friend in friends:
#                 position += friend

#                 if position < weak_point[i+L-1]:
#                     count += 1
#                     position = [w for w in weak_point[i+1:i+L] if w > position][0]
#                 else:
#                     cand.append(count)
#                     break

#     return min(cand) if cand else - 1

def solution(n, weak, dist):
    W, F = len(weak), len(dist)
    repair_lst = [()]
    count = 0
    dist.sort(reverse=True)

    for can_move in dist:
        repairs = []
        count += 1

        for i, wp in enumerate(weak):
            start = wp
            ends = weak[i:] + [n+w for w in weak[:i]]
            can = [end % n for end in ends if end - start <= can_move]
            repairs.append(set(can))

        cand = set()
        for r in repairs:
            for x in repair_lst:
                new = r | set(x)
                if len(new) == W:
                    return count
                cand.add(tuple(new))
        repair_lst = cand

    return -1

n = int(input())
weak = list(map(int, input().split()))
dist = list(map(int, input().split()))

print(solution(n,weak,dist))