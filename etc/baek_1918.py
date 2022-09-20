# 2022/09/20 Baek 1918

string = input()
stack = []
ans =""

for s in string:
  if s.isalpha():
    ans += s
  elif s == "(":
    stack.append("(")
  elif s == "*" or s == "/":
    while stack and (stack[-1] == "*" or stack[-1] == "/"):
      ans += stack.pop()
    stack.append(s)
  elif s == "+" or s == "-":
    while stack and stack[-1] != "(":
      ans += stack.pop()
    stack.append(s)
  elif s == ")":
    while stack and stack[-1] != "(":
      ans += stack.pop()
    stack.pop()

while stack:
  ans += stack.pop()

print(ans)