# 2022/10/31 Baek 1043

# 파티 정보가 나열되는 순서에 따라 오류 발생의 가능성
cnt = 0
N, M = map(int, input().split())
visited = [False] * M

party = []
know_truth = set(list(map(int, input().split()))[1:])
for i in range(M):
  party.append(list(map(int, input().split()))[1:])
  flag = False
  for j in party[i]:
    if j in know_truth:
      flag  = True
      break

  if flag:
    for j in party[i]:
      know_truth.add(j)
    for k in range(i):
      temp = set(party[k]) & know_truth
      if temp and visited[k]:
        for l in party[k]:
          know_truth = know_truth | set(party[k])
        cnt -= 1
        visited[k] = False
  else:
    cnt += 1
    visited[i] = True

print(cnt)
for _ in visited:
  print(_)
print(know_truth)

# 인터넷 참고 코드
# https://ku-hug.tistory.com/148

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []

for _ in range(m):
  parties.append(set(input().split()[1:]))

for _ in range(m):
  for party in parties:
    if party & knowList:
      knowList = knowList | party

cnt = 0
for party in parties:
  if party & knowList:
    continue
  cnt += 1

print(cnt)