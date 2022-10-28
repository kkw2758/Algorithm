# 2022/10/27 Baek 14725

def add(dic, arr):
  if len(arr) == 0:
    return
  if arr[0] not in dic:
    dic[arr[0]] = {}
  add(dic[arr[0]], arr[1:])

def printTree(dic, leng):
  for i in sorted(dic.keys()):
    print("--" * leng + i)
    printTree(dic[i], leng + 1)

N = int(input())
dic = {}
for _ in range(N):
  add(dic, input().split()[1:])

printTree(dic, 0)



