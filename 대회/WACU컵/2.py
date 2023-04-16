# 2023/04/16 WACU컵 2번


score_list = [0 for _ in range(10)]
A, B = map(int,input().split())

cnt = 9
while A > 0:
    if A >= 2 ** cnt:
        score_list[cnt] += 1
        A -= 2 ** cnt
    cnt -= 1

cnt = 9
while B > 0:
    if B >= 2 ** cnt:
        score_list[cnt] += 1
        B -= 2 ** cnt
    cnt -= 1

result = 0
for i in range(len(score_list)):
    if score_list[i] == 1:
        result += 2 ** i

print(result)