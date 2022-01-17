n = int(input())
members = list(map(int, input().split()))
members.sort()

cnt = 0
max_val = 0
result = 0
for idx in range(len(members)):
    cnt += 1
    max_val = max(max_val, members[idx])
    if cnt >= max_val:
        result += 1
        cnt = 0
        max_val = 0

print(result)