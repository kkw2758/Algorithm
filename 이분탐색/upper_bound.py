def uppder_bound(array, start, end, value):
    while start < end:
        mid = start + (end - start)//2
        
        if value < array[mid]:
            end = mid
        else:
            start = mid + 1

    print(start == end)
    return start

array = list(map(int,input().split()))
value = int(input())

print(uppder_bound(array, 0, len(array), value))