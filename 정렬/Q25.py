# def solution(N, stages):
#     answer = []
#     n = len(stages)
#     stages.sort()

#     for i in range(1, N + 1):
#         no_clear_count = 0
#         no_try_count = 0
#         for idx in range(len(stages)):
#             if stages[idx] < i:
#                 no_try_count += 1
#             elif stages[idx] == i:
#                 no_clear_count += 1
#             else:
#                 break
#         if no_try_count == n:
#             answer.append((i, 0))
#             continue
#         answer.append((i, no_clear_count / (n - no_try_count)))
        
#     answer.sort(key = lambda x: x[1], reverse=True)
#     answer = list(map(lambda x: x[0], answer))

#     return answer

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4, 4, 4, 4]))


# def solution(n, stages):
#     stages.sort()
#     probability_list = []
#     for i in range(1, n + 1):
#         numerator = 0
#         denominator = 0
#         for j in stages:
#             if i == j:
#                 numerator += 1
#             if i <= j:
#                 denominator += 1
#         if denominator == 0:
#             probability_list.append((i, 0))
#         else:
#             probability_list.append((i, numerator/denominator))

#     probability_list.sort(reverse=True, key=lambda x : x[1])
#     result = []

#     for i in probability_list:
#         result.append(i[0])

#     return result

# print(solution(5, [2,1,2,6,2,4,3,3]))
# print(solution(4, [4,4,4,4,4]))

def solution(n, stages):
    answer = []
    length = len(stages)

    for i in range(1, n + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key = lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))
