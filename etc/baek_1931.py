# 2022/09/05 Baek 1931


# 첫번째 시작시간으로 정렬을 안해주면 시작시간과 끝나는 시간이 같을 수 있으므로 예외 발생
'''
Ex)
3
8 8
6 8
8 8
2
'''
N = int(input())
meetings = []
for _ in range(N):
  meetings.append(list(map(int, input().split())))

# meetings.sort(key = lambda x: x[0])
meetings.sort(key = lambda x: x[0])
meetings.sort(key = lambda x: x[1])
cnt = 0
before = 0
for start, end in meetings:
  if before <= start:
    before = end
    cnt += 1

print(cnt)