# 2022/12/22 Baek 13908

# 10의 7승 == 10,000,000 > 천만
# M의 볌위가 0 <= M <= N 이므로 M이 0 일때도 고려 해야함
# 그렇지 않으면 EOF 에러
N, M = map(int, input().split())

if M == 0:
  know_number = []
else:
  know_number = list(map(str, input().split()))

result = 0
for i in range(10 ** N):
  num_str = str(i).zfill(N)
  flag = True
  for number in know_number:
    if number not in num_str:
      flag = False
      break
  if flag:
    result += 1

print(result)

# # 백트래킹
N, M = map(int, input().split())
if M == 0:
  know_numbers = []
else:
  know_numbers = list(map(int, input().split()))

print(know_numbers)

def check(password):
  for know_number in know_numbers:
    if know_number not in password:
      return False
  return True

result = 0

def dfs(password):
  global result
  if len(password) == N:
    print(password)
    if check(password):
      result += 1
    return
  for i in range(10):
    password.append(i)
    dfs(password)
    password.pop()

dfs([])
print(result)
