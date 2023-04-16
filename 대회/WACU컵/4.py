# 2023/04/16 WACU컵 4번

N = int(input())
target_string = input()

def check(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1

    return cnt

if target_string[0] != target_string[-1]: # 처음과 끝이 다르면
    print("YES")
else: #처음과 끝이 같으면.
    for i in range(1, N):
        if check(target_string[:i], target_string[-i:]) == 1:
            print("YES")
            break
    else:
        print("NO")

