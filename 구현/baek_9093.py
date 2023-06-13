# 2023/06/13 Baek 9093


# 방법 1 - for문
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    result = ""
    temp = ""
    sentence = input().strip()
    for s in sentence:
        if s == " ":
            temp += s
            result += temp
            temp = ""
        else:
            temp = s + temp

    print(result + temp)

# 방법 2 - while문
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sentence = list(input().strip())
    i = 0
    while i < len(sentence):
        if sentence[i] == " ":
            i += 1
        else:
            start = i
            while i < len(sentence) and sentence[i] != " ":
                i += 1
            temp = sentence[start:i]
            temp.reverse()
            sentence[start:i] = temp

    print("".join(sentence))