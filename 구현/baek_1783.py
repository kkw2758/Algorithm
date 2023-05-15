# 2023/05/12 Baek 1783

# 2칸 위로, 1칸 오른쪽
# 1칸 위로, 2칸 오른쪽
# 1칸 아래로, 2칸 오른쪽
# 2칸 아래로, 1칸 오른쪽

# 체스판의 가장 왼쪽 아래 칸에 위치해 있음
# 방문한 칸의 수를 최대로
# 이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용
# 이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법 제한 x

N, M = map(int, input().split())


# N 세로
# M 가로
def solution():
    if N == 1:
        print(1)
    elif N == 2:
        print(min(4, (M + 1) // 2))
    else:
        if M <= 6:
            print(min(4, M))
        else:
            print(M - 2)
            
solution()