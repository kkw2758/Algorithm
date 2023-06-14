# 2023/06/14 Baek 2960

# 풀이 1
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 입력받은 수 n에 대해서 소수인지 판별하는 함수
def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

# 문제에서 제시한 알고리즘을 실행하는 함수
def solution(N, K):
  numbers = [i for i in range(2, N + 1)]

  cnt = 0
  while numbers:
    P = 0
    for number in numbers:
        # 소수를 찾으면 그 수를 P에 저장한다.
        if is_prime(number):
            P = number
            break
    # P의 배수를 제거하는 과정
    for number in range(P, N + 1, P):
        if number in numbers:
            numbers.remove(number)
            cnt += 1
            # K 번째 제거할때 해당 제거하는 수를 출력
            if cnt == K:
                print(number)
                return

solution(N,K)


# 풀이 2
N, K = map(int, input().split())
numbers = [True] * (N + 1)

cnt = 0
for i in range(2, len(numbers)):
    if numbers[i]:
        for j in range(i, N + 1, i):
            if numbers[j]:
                numbers[j] = False
                cnt += 1
                if cnt == K:
                    print(j)
                    break