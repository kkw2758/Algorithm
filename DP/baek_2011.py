# 2022/09/29 Baek 2011

# 내가 작성한 코드 >> 복잡하다.
code = input()
def solution(code):
  n = len(code)
  dp = [0] * 5001
  if 1 <= int(code[:1]) <= 9:
    dp[1] += 1
    if n >= 2:
      if 10 <= int(code[:2]) <= 26:
        dp[2] += 1
      if 1 <= int(code[1]) <= 9:
        dp[2] += 1  
    
  for i in range(3, n + 1):
    if 10 <= int(code[i - 2: i]) <= 26:
      dp[i] += dp[i - 2]
    if 1 <= int(code[i - 1: i]) <= 9:
      dp[i] += dp[i - 1]


    dp[i] %= 1000000
  return dp[n]
print(solution(code))

# 개선한 나의 코드
code = input()
def solution(code):
  n = len(code)
  dp = [0] * 5001
  if code[0] == "0":
    return "0"
  dp[0] = 1
  dp[1] = 1

  for i in range(2, n + 1):
    if 10 <= int(code[i - 2: i]) <= 26:
      dp[i] += dp[i - 2]
    if 1 <= int(code[i - 1: i]) <= 9:
      dp[i] += dp[i - 1]


    dp[i] %= 1000000
  return dp[n]
print(solution(code))

# 인터넷 참고 풀이
# 출처 : https://jyeonnyang2.tistory.com/55
n = list(map(int, input()))
l = len(n)
dp = [0 for _ in range(l + 1)]
if (n[0] == 0):
  print("0")
else:
  n = [0] + n
  dp[0] = 1
  dp[1] = 1
  for i in range(2, l + 1):
    if n[i] > 0:
      dp[i] += dp[i - 1]
    temp = n[i - 1] * 10 + n[i]
    if 10 <= temp <= 26:
      dp[i] += dp[i - 2]
  print(dp)
  print(dp[l] % 1000000)