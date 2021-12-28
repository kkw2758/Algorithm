'''
<두 배열의 원소 교체>
동빈이는 두개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야한다.

N, K, 그리고 배열 A 와 B의 정보가 주어졌을 떄, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 a의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

입력조건
첫 번째 줄에 N, K가 공백으로 구분되어 입력된다. (1 <= N <= 100,000, 0 <= k <= N)
두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.

출력조건
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.
'''

n, k = map(int,(input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort(reverse=True)

for idx in range(k):
    if a[idx] < b[idx]:
        #a[idx] = b[idx]
        a[idx], b[idx] = b[idx], a[idx]
    else:
        break

print(sum(a))

# 내가 생각한풀이
# A를 오름차순으로 정렬, B를 내림차순으로 정렬
# B의 최댓값과 A의 최솟값을 비교하여 B의 최댓값이 A의 최솟값보다 크면 바꾸고 그게 아니라면 B의 값이 A의 최솟값보다 전부 작다는 뜻이므로 바꿀필요가없다.


n, k = map(int, input().split())
A = [x for x in list(map(int, input().split()))]
B = [x for x in list(map(int, input().split()))]


A.sort()
B.sort(reverse=True)
for idx in range(k):
    if A[idx] < B[idx]:
        A[idx], B[idx] = B[idx], A[idx]
    else:
        break

print(sum(A))