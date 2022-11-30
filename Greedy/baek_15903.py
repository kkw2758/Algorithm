# 2022/11/30 Baek 15903
import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
q = []
for card in cards:
  heapq.heappush(q, card)

for i in range(m):
  first = heapq.heappop(q)
  second = heapq.heappop(q)
  value = first + second
  for j in range(2):
    heapq.heappush(q, value)

print(sum(q))