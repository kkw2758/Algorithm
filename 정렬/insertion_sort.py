'''
array = [7, 5, 9, 0, 3]

def find_ins_idx(sorted_array,value):
    for idx in range(len(sorted_array)):
        if value < sorted_array[idx]:
            return idx

    return len(sorted_array)


def insertion_sort(array):
    for i in range(1, len(array)):
        value = array.pop(i)
        idx = find_ins_idx(array[:i], value)
        array.insert(idx, value)
    return array

print(insertion_sort(array))
'''

array = [7, 5, 9, 0, 3]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)


array = [2, 1 , 8, 4, 6]

for i in range(1, len(array)):
    key = array[i]
    # j의값은 기준이되는 값의 바로 왼쪽 인덱스
    j = i -1
    
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1

    array[j + 1] = key

print(array)
    