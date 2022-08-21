n, c = map(int, input().split())
house_list = []
for _ in range(n):
  house_list.append(int(input()))

house_list.sort()
start = 1
end = house_list[-1] - house_list[0]

result = 0
while start <= end:
  mid = (start + end) // 2
  value = house_list[0]
  count = 1
  for i in range(1, n):
    if house_list[i] >= value + mid:
      count += 1
      value = house_list[i]

  if count >= c:
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)       
