# 2022/11/08 Baek 1026

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
print(A)
print(B)

result = 0
for i in range(N):
  result += A[i] * B[i]

print(result)