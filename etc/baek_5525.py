# 2022/09/07 Baek 5525

N = int(input())
M = int(input())
S = input()

PN = "IO" * N + "I"


result = 0
while True:
  idx = S.find(PN)
  if idx == -1:
    break
  S = S[idx + 1:]
  result += 1

print(result)

#===========================
N = int(input())
M = int(input())
S = input()

answer, i, count = 0, 0, 0

while i < (M - 1):
  if S[i:i + 3] == "IOI":
    i += 2
    count += 1
    if count == N:
      answer += 1
      count -= 1
  else:
    i += 1
    count = 0

print(answer)