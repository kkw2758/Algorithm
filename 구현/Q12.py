def is_possible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif a == 1:    # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False

    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:      # 삭제
            answer.remove([x, y, a])
            if not is_possible(answer):
                answer.append([x, y, a])
        elif b == 1:    # 추가
            answer.append([x, y, a])
            if not is_possible(answer):
                answer.remove([x, y, a])

    answer = sorted(answer)
    return answer



n = int(input())
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n, build_frame))

def is_possible(frames):
    for frame in frames:
        x, y, a = frame
        if a == 0: # 기둥일때
            if not(y == 0 or [x - 1, y , 1] in frames or [x, y, 1] in frames or [x, y - 1, 0] in frames):
                return False
        elif a == 1:
            if not([x, y - 1, 0] in frames or [x + 1, y - 1, 0] in frames or ([x - 1, y, 1] in frames and [x + 1, y, 1] in frames)):
                return False

    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:
            answer.append([x, y, a])
            if not(is_possible(answer)):
                answer.remove([x, y, a])
        elif b == 0:
            print(frame)
            answer.remove([x, y, a])
            if not(is_possible(answer)):
                answer.append([x, y, a])


    answer.sort()
    return answer

n = int(input())
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# build_frame = [[0,0,0,1], [2,0,0,1], [4,0,0,1], [0,1,1,1], [1,1,1,1], [2,1,1,1], [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1]]

print(solution(n, build_frame))