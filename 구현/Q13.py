from itertools import combinations

n, m = map(int, input().split())

chicken, house = [], []

for row in range(n):
    temp = list(map(int, input().split()))
    for col in range(len(temp)):
        if temp[col] == 1:
            house.append((row + 1, col + 1)) 
        if temp[col] == 2:
            chicken.append((row + 1, col + 1))


candidates = list(combinations(chicken, m))

def get_total_chicken_distance(candiate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candiate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_total_chicken_distance(candidate))

print(result)

'''
ex1)
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

ex2)
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

ex3)
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
'''

from itertools import combinations
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))

chicken_houses = []
for row in range(n):
    for col in range(n):
        if board[row][col] == 2:
            chicken_houses.append((row, col))

candidates = combinations(chicken_houses, m)

result = INF

for candidate in candidates:
    total_chicken_distance = 0
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                chicken_distance = INF
                for i in candidate:
                    temp = abs(row - i[0]) + abs(col - i[1])
                    chicken_distance = min(chicken_distance, temp)

                total_chicken_distance += chicken_distance
    
    result = min(result, total_chicken_distance)

print(result)