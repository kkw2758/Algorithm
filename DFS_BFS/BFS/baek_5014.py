import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int,input().split())
building = [0] * (F + 1)

def bfs(start_stair, target_stair):
    queue = deque()
    queue.append(start_stair)

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

print(bfs(S, G))
print(building)