array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return

    pivot = start   # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)



array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))



def quick_sort(array):
    n = len(array)
    if n == 1 or n == 0:
        return array
    pivot = array[0]
    left = 1
    right = n-1
    while left <= right:
        # for x in range(1,n):
        #     if pivot > array[x]:
        #         left += 1
        #     else:
        #         break
        
        # for y in range(n-1,0,-1):
        #     if pivot < array[y]:
        #         right -= 1
        #     else:
        #         break
        while left <= n-1 and array[left] <= array[0]:
            left += 1
        
        while right > 0 and array[right] >= array[0]:
            right -=1


        if left < right:
            array[left],array[right] = array[right],array[left]
        else:
            array[0],array[right] = array[right],array[0]

        print(left,right)
        print(array)

    return quick_sort(array[:right]) + [array[right]] + quick_sort(array[right+1:])

print(quick_sort([5,7,9,3,0]))