# 2023/05/11 Baek 10809

S = input()

for i in range(26):
    if chr(i + 97) in S:
        print(S.find(chr(i + 97)), end = " ")
    else:
        print(-1, end = " ")