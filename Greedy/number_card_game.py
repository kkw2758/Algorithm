
n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
max_card_number = 0

for row in matrix:
    min_num_in_row = min(row)
    if max_card_number < min_num_in_row:
        max_card_number = min_num_in_row

print(max_card_number)


n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

max_card_number = 0
for row in matrix:
    min_card_in_row = row[0]
    for col in row[1:]:
        if min_card_in_row > col:
            min_card_in_row = col
    max_card_number = max(max_card_number, min_card_in_row)

print(max_card_number)