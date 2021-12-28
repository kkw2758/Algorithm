'''
unsorted_array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0 ,5 ,2]

max_member = max(unsorted_array)
min_member = min(unsorted_array)

array = [0 for x in range(max_member - min_member + 1)]


for member in unsorted_array:
    # min_index에 해당하는 값이 카운트되는 인덱스가 array배열의 첫번째 인덱스가 되도록 조절하는 과정
    # member - min_member
    idx = member - min_member
    array[idx] += 1


for idx in range(len(array)):
    for x in range(array[idx]):
        print(idx + min_member, end = " ")
 '''



MAX_NUM = 20

A = list(map(int, input().split()))

N = len(A)

#입력받은 리스트 A의 값을 카운트해줄 리스트
count = [0] * (MAX_NUM + 1)
#누적합을 저장하는 배열
countSum = [0]*(MAX_NUM + 1)


for i in range(N):
    count[A[i]] += 1

countSum[0] = count[0]
for i in range(1, MAX_NUM + 1):
    countSum[i] = countSum[i - 1] + count[i]

print("count = ",count)
print("countSum = ",countSum)

#누적합 카운트 때문에 B의크기를 편의상 N + 1로 맞춰줌
B = [0]*(N + 1)

for i in range(N - 1, -1, -1):
    B[countSum[A[i]]] = A[i]
    countSum[A[i]] -= 1

print(B)



def count_sort(array):
    max_value = max(array)
    min_value = min(array)
    n = max_value - min_value + 1

    tmp_list = [0 for x in range(n)]
    for member in array:
        tmp_list[member-min_value] += 1

    for member in range(len(tmp_list)):
        if tmp_list[member] != 0:
            for x in range(tmp_list[member]):
                print(member + min_value, end = " ")


count_sort([7,5,9,0,3,1,6,2,9,1,4,8,0,5,2])