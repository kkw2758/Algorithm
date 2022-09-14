# 2022/09/14 Baek 1991

import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = {}
for _ in range(N):
  start, left, right = list(input().split())
  tree[start] = [left, right]

def pre(now):
  if now != ".":
    print(now, end = "")
    pre(tree[now][0])
    pre(tree[now][1])

def middle(now):
  if now != ".":
    middle(tree[now][0])
    print(now, end = "")
    middle(tree[now][1])

def end(now):
  if now != ".":
    end(tree[now][0])
    end(tree[now][1])
    print(now, end = "")

pre("A")
print("")
middle("A")
print("")
end("A")