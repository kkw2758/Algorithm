def uppder_bound(array, start, end, value):
    while start < end:
        mid = start + (end - start)//2
        
        if array[mid] > value:
            end = mid
        else:
            start = mid + 1

    return start

array = list(map(int,input().split()))
value = int(input())

print(uppder_bound(array, 0, len(array), value))