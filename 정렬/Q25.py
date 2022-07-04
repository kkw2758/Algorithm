def solution(N, stages):
    answer = []
    n = len(stages)
    stages.sort()

    for i in range(1, N + 1):
        no_clear_count = 0
        no_try_count = 0
        for idx in range(len(stages)):
            if stages[idx] < i:
                no_try_count += 1
            elif stages[idx] == i:
                no_clear_count += 1
            else:
                break
        if no_try_count == n:
            answer.append((i, 0))
            continue
        answer.append((i, no_clear_count / (n - no_try_count)))
        
    answer.sort(key = lambda x: x[1], reverse=True)
    answer = list(map(lambda x: x[0], answer))

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4]))