# 2022/11/17 baek_16401

M, N = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def binary_search(start, end):
    global result
    while start <= end:

        mid = (start + end) // 2
        cnt = 0
        for i in range(N - 1, -1, -1):
            if arr[i] < mid:
                break
            cnt += arr[i] // mid
        if cnt >= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

result = 0
binary_search(1, max(arr))
print(result)