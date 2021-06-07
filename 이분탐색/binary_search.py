# 인자값 - 시작점, 끝점, 찾을 값, 리스트
# 반환값  - 찾을값의 인덱스, 찾는값이 없다면 없다는 것을 표현하는 문구

# 재귀함수를 이용
def recursive_binary_search(array, start, end, value):
    if start > end:
        return "-NOT FOUND-"

    mid = (start + end) // 2

    if array[mid] == value:
        return mid
    elif array[mid] > value:
        return recursive_binary_search(array, start, mid - 1, value)
    else:
        return recursive_binary_search(array, mid + 1, end, value)

n, value = map(int, input().split())
array = list(map(int,input().split()))

print(recursive_binary_search(array, 0, n - 1, value))


# 반복문을 이용
def binary_search(array, start, end, value):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == value:
            return mid
        elif array[mid] > value:
            end = mid - 1
        else:
            start = mid + 1

    return "-NOT FOUND-"

n, value = map(int, input().split())
array = list(map(int,input().split()))

print(binary_search(array, 0, n - 1, value))