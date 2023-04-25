# 2023/04/25 Baek 27967

import sys
input = sys.stdin.readline

N = int(input())
target_string = input()

def back(string, start):
    if len(string) == N:
        flag = 0
        for i in string:
            if i == "(":
                flag += 1
            else:
                flag -= 1
                if flag < 0:
                    break
        if flag == 0:
            print(string)
            sys.exit(0)
        return
    
    for i in range(start, N):
        if target_string[i] == "G":
            back(string + ")", i + 1)
            back(string + "(", i + 1)
        else:
            back(string + target_string[i], i + 1)

back("", 0)

import sys
input = sys.stdin.readline

N = int(input())
target_string = input()
a = N // 2
for i in target_string:
    if i == "(":
        a -= 1
for i in target_string:
    if i == "G":
        if a > 0:
            print("(", end="")
            a -= 1
        else:
            print(")", end="")
    else:
        print(i, end="")