array = [3,2,5,8,6,7]

def selection_sort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i,len(array)):
            if array[j] < array[min_idx]:
                min_idx = j

        array[min_idx],array[i] = array[i], array[min_idx]
    return array

print(selection_sort(array))
