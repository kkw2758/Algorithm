def rotate_90(matrix):
    n = len(matrix)
    m = len(matrix[0])

    ret = [[0] * n for _ in range(m)]

    for r in range(n):
        for c in range(m):
            ret[c][n - 1 - r] = matrix[r][c]

    return ret

# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# print(rotate_90(matrix))



n, m = map(int, input().split())

lock = [ list(map(int, input().split())) for _ in range(n)]
key = [ list(map(int, input().split())) for _ in range(m)]

def solution(key, lock):
    answer = False
    zero_list = []

    for x in range(len(lock)):
        for y in range(len(lock[0])):
            if lock[x][y] == 0:
                zero_list.append((x,y))
    zero_list.sort()

    for _ in range(4):
        key = rotate_90(key)
        one_list = []
        for x in range(len(key)):
            for y in range(len(key[0])):
                if key[x][y] == 1:
                    one_list.append((x,y))

        # print("one_list={}".format(one_list))
                    
        for dr in range(-m + 1, m):
            for dc in range(-m + 1, m):
                tmp = []
                for member in one_list:
                    nr = member[0] + dr
                    nc = member[1] + dc
                    if 0 <= nc < m and 0 <=nr < m:
                        tmp.append((nr,nc))
                tmp.sort()
                # if dr == 1 and dc == 1 and _ == 0:
                #     print(tmp == zero_list)
                #     print(tmp)
                if zero_list == tmp:
                    answer = True
                    print(tmp)
                    return answer

    return answer

print(solution(key,lock))

def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                if check(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False