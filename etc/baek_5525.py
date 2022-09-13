# 2022/09/07 Baek 5525

# 시간 초과 방지
# 파이썬에서 arr [a:b]의 시간 복잡도는 O(b - a)라고 한다.
# 슬라이스를 최대한 덜 쓰고 반복을 최소화하는 방법을 찾아야 한다.
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

PN = "IO" * N + "I"

result = 0
for i in range(M - (2 * N + 1)):
  if S[i:i + (2 * N + 1)] == PN:  
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