'''
<위에서 아래로>

하나의 수열에는 다양한 수가 조냊한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이수를 큰수부터 작은 수의 순서로 정렬해야한다.
수열을 내림차순으로 정렬하는 프로그램을 만드시오

입력조건
첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1 <= N <= 500)
둘째 줄부터 N + 1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1이상 100,000 이하의 자연수이다.

출력조건
입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공배긍로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.
'''


n = int(input())

array = [int(input()) for _ in range(n)]
array.sort(reverse = True)

for member in array:
    print(member, end = " ")



n = int(input())
tmp_list = []
for _ in range(n):
    tmp_list.append(int(input()))

tmp_list.sort(reverse=True)

for idx in range(len(tmp_list)):
    print(tmp_list[idx], end = " ")
