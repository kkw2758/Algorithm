# 2022/11/17 baek_10815

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
targets = list(map(int, input().split()))

def binary_search(start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(start, mid - 1, target)
    else:
        return binary_search(mid + 1, end, target)

for target in targets:
    if binary_search(0, N - 1, target) == -1:
        print(0, end = " ")
    else:
        print(1, end = " ")