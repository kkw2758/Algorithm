def lower_bound(array, start, end, value):
    while start < end:
        mid = (start + end) // 2

        if array[mid] >= value:
            end = mid
        else:
            start = mid + 1
    return start

array = list(map(int, input().split()))
target = int(input())

print(lower_bound(array, 0, len(array), target))