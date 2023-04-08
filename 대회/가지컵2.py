import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
floor = [0] * 100001

total = 0
for i in range(1, M + 1):
    t, r = map(int, input().split())
    floor[t] += r
    total += r
    if total > K:
        break
    
if total > K:
    print(i, 1)
else:
    print(-1)