dp = [0 for _ in range(26)]
word1 = input()
word2 = input()

for i in word1:
  idx = ord(i) - 97
  dp[idx] += 1

for j in word2:
  idx = ord(j) - 97
  dp[idx] -= 1

print(dp)

plus = 0
minus = 0
for i in dp:
  if i > 0 :
    plus += i
  elif i < 0 :
    minus += i

result = max(plus, abs(minus))
print(result)