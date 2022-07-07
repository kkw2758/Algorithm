import itertools
l, c = map(int, input().split())

alphas = list(input().split())
alphas.sort()
mo = ["a", "e", "i", "o", "u"]

for password in itertools.combinations(alphas, l):
  count = 0
  for string in password:
    if string in mo:
      count += 1
  if count >= 1 and count <= l - 2:
    password = "".join(password)
    print(password)