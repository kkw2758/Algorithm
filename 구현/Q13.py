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