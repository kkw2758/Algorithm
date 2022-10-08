# 2022/10/08 Baek 15681

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
connect = [[] for _ in range(N + 1)]

for _ in range(N - 1):
  U, V = map(int, input().split())
  connect[U].append(V)
  connect[V].append(U)

child = [[] for _ in range(N + 1)]
size = [0] * (N + 1)

def makeTree(currentNode, parent):
  for Node in connect[currentNode]:
    if Node != parent:
      child[currentNode].append(Node)
      makeTree(Node, currentNode)

def countSubtreeNodes(currentNode):
  size[currentNode] = 1
  for Node in child[currentNode]:
    countSubtreeNodes(Node)
    size[currentNode] += size[Node]

makeTree(R, -1)
countSubtreeNodes(R)
for _ in range(Q):
  query = int(input())
  print(size[query])
