# 2022/09/04 Baek 1074

# N의 크기에 따라 배열의 크기를 잡으면
# 배열의 크기가 최대 2**16이되어서 메모리 초과 발생
N, r, c = map(int, input().split())

graph = [[0] * (2 ** N + 1) for _ in range(2 ** N + 1)]
def func(n, first, start_x, start_y):
  if n == 1:
    graph[start_x][start_y] = first
    graph[start_x][start_y + 1] = first + 1
    graph[start_x + 1][start_y] = first + 2
    graph[start_x + 1][start_y + 1] = first + 3
  else:
    func(n - 1, first, start_x, start_y)
    func(n - 1, first + 4 ** (n - 1), start_x, start_y + 2**(n-1))
    func(n - 1, first + 4 ** (n - 1) * 2, start_x + 2**(n-1), start_y)
    func(n - 1, first + 4 ** (n - 1) * 3, start_x + 2**(n-1), start_y + 2**(n-1))


func(N, 0, 1, 1)
print(graph[r+1][c+1])

# 1,2,3,4 사분면 나누어서 생각해주자
N, r, c = map(int, input().split())

ans = 0
while N != 0:
  N -= 1
  if r < 2 ** N and c < 2 ** N:
    ans += (2 ** N) * (2 ** N) * 0
  elif r < 2 ** N and c >= 2 ** N:
    ans += (2 ** N) * (2 ** N) * 1
    c -= (2 ** N)
  elif r >= 2 ** N and c < 2 ** N:
    ans += (2 ** N) * (2 ** N) * 2
    r -= (2 ** N)
  else:
    ans += (2 ** N) * (2 ** N) * 3
    c -= (2 ** N)
    r -= (2 ** N)

print(ans)