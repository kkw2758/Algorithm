data = [10, 20, 30, 40, 50]
P = [0] * (len(data) + 1)

for i in range(len(data)):
  sum = 0
  for j in range(i + 1):
    sum += data[j]
  P[i + 1] = sum

left = int(input())
right = int(input())

result = P[right] - P[left -1]
print(result)

data = [10, 20, 30, 40, 50]
sum_value = 0
prefix_sum = [0]
for i in data:
  sum_value += i
  prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])