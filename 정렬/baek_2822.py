# 2023/02/15 Baek 2822

numbers = []
for i in range(1,9):
  numbers.append((int(input()),i))

numbers.sort()
numbers = numbers[3:]
numbers.sort(key= lambda x:x[1])

sum = 0
score_list = []
for number, cnt in numbers:
  sum += number
  score_list.append(str(cnt))
print(sum)
print(" ".join(score_list))