n = int(input())
li = list(map(int, input().split()))

target = 1
li.sort()

for x in li:
    if target < x:
        break
    else:
        target += x

print(target)