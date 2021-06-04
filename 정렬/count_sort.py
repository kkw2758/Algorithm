unsorted_array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0 ,5 ,2]

max_member = max(unsorted_array)

array = [0 for x in range(max_member + 1)]

for idx in unsorted_array:
    array[idx] += 1

for idx in range(len(array)):
    for x in range(array[idx]):
        print(idx, end = " ")
