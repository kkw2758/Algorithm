import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int,input().split())
building = [0] * (F + 1)

def bfs(start_stair, target_stair):
    queue = deque()
    queue.append(start_stair)
    building[start_stair] = 1
    while queue:
        now = queue.popleft()
        if now == target_stair:
            return building[now] - 1

        up = now + U
        if 0 < up < F + 1 and not building[up]:
            building[up] = building[now] + 1
            queue.append(up)

        down = now - D
        if 0 < down < F + 1 and not building[down]:
            building[down] = building[now] + 1
            queue.append(down)

    return "use the stairs"

print(bfs(S, G))
print(building)

'''
# 오답코드
# 시작하는 구간을 밤운 처리안하고 다른구간을 방문하는데
# 어차피 갈 수 있는 모든지점 방문후 방문한구역을 확인해보면 시작지점빼고 값이 올바르게 나오는데 왜틀렸는지 모르겠다.
import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int,input().split())
building = [0] * (F + 1)

def bfs_1(start_stair, target_stair):
    queue = deque()
    queue.append(start_stair)
    #building[start_stair] = 1
    while queue:
        now = queue.popleft()
        if now == target_stair:
            return building[now]

        up = now + U
        if 0 < up < F + 1 and not building[up]:
            building[up] = building[now] + 1
            queue.append(up)

        down = now - D
        if 0 < down < F + 1 and not building[down]:
            building[down] = building[now] + 1
            queue.append(down)

    return "use the stairs"

print(bfs_1(S, G))
print(building)
'''