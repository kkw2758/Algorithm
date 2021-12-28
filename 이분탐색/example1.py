'''
<부품 찾기>
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 M개 종류의 부품을 대량으로 구메하겠다며 당일 날 견적서를 요청했다.
동빈이는 떄를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로한다.

입력조건
첫째 줄에 정수 N이 주어진다. (1 <= N <= 1,000,000)
둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100,000)
넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000, 이하이다.

출력조건
첫째 줄에 공배긍로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
'''

'''
<일반적인 풀이를 하였을때>
첫째 줄에 정수 N이 주어진다. (1 <= N <= 1,000,000)
둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100,000)
넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000, 이하이다.

이진탐색의 시간복잡도 O(logN)
파이썬 라이브러리의 정렬을 이용했을때 시간복잡도 O(NlogN)
따라서 이진 탐색을 사용하는 경우 시간복잡도 O((M + N) * logN)

N, M 이 최대일때 시간복잡도
N = 1,000,000 이면 n_list를 정렬하는데 1,000,000 * log 1,000,000 = 20,000,000
M = 100,000 이면 log 1,000,000 * 100,000 = 2,000,000
위 내용을 보면 최대 2,000만으로 더욱더 많은 연산이 팔요한 것을 알 수 있다.
'''
import time

start = time.time()

n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()


m = int(input())
m_list = list(map(int,input().split()))


def recursive_binary_search(start, end, target, array):
    if start > end:
        return "no"

    mid = (start + end)//2

    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return recursive_binary_search(start, mid - 1, target, array)
    else:
        return recursive_binary_search(mid + 1, end, target, array)

for target in m_list:
    print(recursive_binary_search(0,n - 1, target, n_list), end = " ")


print("\ntime :", time.time() - start)


# 이진탐색을 반복문으로 구현한 함수를 이용해서 풀이
# def binary_search(start, end, target, array):
#     while start <= end:
#         mid = (start + end) // 2
        
#         if array[mid] == target:
#             return "yes"
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1

#     return "no"

# for target in m_list:
#     print(binary_search(0,n - 1, target, n_list), end = " ")




'''
위의 풀이가 최대 2,000만 회보다 많은 연산이 필요할 수 있다는 것을 인지
어떻게하면 연산 수 를 줄일 수 있을까? -> 정렬할 범위의 수가 정수처럼 딱딱떨어지고 크기가 정해져있을때? 계수정렬을 이용해서 정렬한번 해볼까?
계수정렬의 시간복잡도 -> 정렬해야할 멤버수 = N, 정렬해야할 멤버중 가장큰 값 = K, 시간복잡도 = O(N + K)

N과 M이 최대일떄 시간복잡도
n_list(n_list의 최댓값 = 1,000,000 이라 가정)를 계수정렬을 이용해서 정렬 -> 2,000,000
M이 최대일때 이분탐색 -> log 1,000,000 * 100,000 = 2,000,000
최대 연산횟수 약 4,000,000 위의 파이썬 내장 라이브러리를 이용하는것보다 무려 연산횟수가 5배이상 차이가난다!
'''

start = time.time()

# 계수정렬을 이용하여 전자매장의 부품을 정렬하고 이진탐색을 이용한 풀이.
def count_sort(unsorted_array):
    max_value = max(unsorted_array)
    temp = [0] * (max_value + 1)

    for member in unsorted_array:
        temp[member] += 1

    result = []
    for count in range(len(temp)):
        for i in range(temp[count]):
            result.append(count)

    return result

def recursive_binary_search(start, end, target, array):
    if start > end:
        return "no"

    mid = (start + end)//2

    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return recursive_binary_search(start, mid - 1, target, array)
    else:
        return recursive_binary_search(mid + 1, end, target, array)


n = int(input())
n_list = list(map(int,input().split()))
n_list = count_sort(n_list)


m = int(input())
m_list = list(map(int,input().split()))

for target in m_list:
    print(recursive_binary_search(0,n - 1, target, n_list), end = " ")

print("\ntime :", time.time() - start)


# 계수 정렬의 개념을 이용한 풀이
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if array[i] == 1:
        print("yes", end = " ")
    else:
        print("no", end = " ")

print("")

# 집합을 이용한 풀이
n = int(input())
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in array:
        print("yes", end = " ")
    else:
        print("no", end = " ")


n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def recursive_binary_search(sorted_array, start, end, target):
    if start > end:
        return False

    mid = (start + end)//2
    if sorted_array[mid] == target:
        return mid
    elif sorted_array[mid] > target:
        return recursive_binary_search(sorted_array, start, mid-1, target)
    else:
        return recursive_binary_search(sorted_array, mid + 1, end, target)

for m in m_list:
    if recursive_binary_search(n_list, 0, n-1,m):
        print("yes", end=" ")
    else:
        print("no", end=" ")

def count_sort(array):
    max_value = max(array)
    min_value = min(array)
    tmp_list = [0 for _ in range(max_value - min_value + 1)]
    result_list = []
    
    for idx in range(len(array)):
        tmp_list[array[idx] - min_value] += 1

    for i in range(len(tmp_list)):
        for j in range(tmp_list[i]):
            result_list.append(i + min_value)

    return result_list

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list = count_sort(n_list)

def recursive_binary_search(sorted_array, start, end, target):
    if start > end:
        return False

    mid = (start + end)//2
    if sorted_array[mid] == target:
        return mid
    elif sorted_array[mid] > target:
        return recursive_binary_search(sorted_array, start, mid-1, target)
    else:
        return recursive_binary_search(sorted_array, mid + 1, end, target)

for m in m_list:
    if recursive_binary_search(n_list, 0, n-1,m):
        print("yes", end=" ")
    else:
        print("no", end=" ")