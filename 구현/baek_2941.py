# 2023/01/25 Baek 2941

alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in alpha:
  word = word.replace(i, "*")
print(len(word))