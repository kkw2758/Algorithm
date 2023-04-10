# 2023/04/11 Baek 1337

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
  
numbers.sort()
# 중복되는 수 없음
# 배열을 순회하면서 차이가 5보다 작으면서 가장 긴 구간을 찾는다.
# 5 - 구간의 길이가 답

end = 1
interval = 1
for i in range(N):
    while end < N and numbers[end] - numbers[i] < 5:
        interval = max(interval, end - i + 1)
        end += 1
        
print(5 - interval)