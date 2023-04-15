# 1
n = int(input())
colors = list(input().split())
m, k = map(int, input().split())

candidate = []

for _ in range(m):
    assist = list(map(int,input().split()))
    temp = []
    for i in assist:
        temp.append(colors[i - 1])
    if "P" in temp:
        candidate.append("P")
    else:
        candidate.append("W")


if "W" in candidate:
    print("W")
else:
    print("P")