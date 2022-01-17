n, m = map(int, input().split())
li = list(map(int, input().split()))

li.sort()
result = 0

for x in range(len(li) - 1):
    for y in range(x + 1, len(li)):
        if li[x] != li[y]:
            result += 1

print(result)