import sys
input = sys.stdin.readline

def find_max_idx(li):
    max_idx = 0
    for i in range(1, len(li)):
        if li[i] > li[max_idx]:
            max_idx = i

    return max_idx

N = int(input())
board = [[0] * (N + 2)] 
for _ in range(N):
    board.append([0] + list(map(int, input().strip().split())) + [0])
board +=  [[0] * (N + 2)]
x1, y1, x2, y2 = N//2, N//2, N//2 + 1, N//2 + 1
# UDLR
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = "UDLR"
total = 0
course = ""
while True:
    nutriment = [0, 0, 0, 0]
    # U
    for i in range(y1, y2 + 1):
        nutriment[0] += board[x1 - 1][i]
    # D
    for i in range(y1, y2 + 1):
        nutriment[1] += board[x2 + 1][i]
    # L
    for i in range(x1, x2 + 1):
        nutriment[2] += board[i][y1 - 1]
    #R
    for i in range(x1, x2 + 1):
        nutriment[3] += board[i][y2 + 1]
    
    max_idx = find_max_idx(nutriment)
    if nutriment[max_idx] <= 0:
        print(total)
        print(course)
        break
    else:
        total += nutriment[max_idx]
        course += direction[max_idx]
        if max_idx == 0:
            x1 -= 1
        elif max_idx == 1:
            x2 += 1
        elif max_idx == 2:
            y1 -= 1
        elif max_idx == 3:
            y2 += 1

        
