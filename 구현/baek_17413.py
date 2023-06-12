# 2023/06/12 Baek 17413

text = input()
result = ""

flag = False
temp = ""

for s in text:
    if flag == False:
        if s == "<":
            flag = True
            temp += s
        elif s == " ":
            temp += s
            result += temp
            temp = ""
        else:
            temp = s + temp

    elif flag == True:  # 괄호 안에 있으면
        if s == ">":
            flag = False
            temp += s
            result += temp
            temp = ""
        else:
            temp += s

print(result + temp)

import sys
input = sys.stdin.readline

text = list(input().strip())
i = 0
start = 0

while i < len(text):
    if text[i] == "<": # 괄호 안은 뒤집지 않는다.
      # 괄호가 끝날 때 까지
      while text[i] != ">":
          i += 1
      i += 1
    elif text[i] == " ": # 공백은 그대로
        i += 1
    else: # 단어가 끝날때 까지 i를 증가시키고 뒤집는다
        start = i
        while i < len(text) and text[i].isalnum():
            i += 1
        temp = text[start:i]
        temp.reverse()
        text[start:i] = temp
        
print("".join(text))