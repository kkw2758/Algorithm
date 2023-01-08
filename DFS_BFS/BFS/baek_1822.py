# 2022/11/17 baek_1822

n_A, n_B = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort()

result = []
def binary_search(start, end, target):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if B[mid] == target:
        return mid
    elif B[mid] > target:
        return binary_search(start, mid - 1, target)
    else:
        return binary_search(mid + 1, end, target)

for target in A:
    if binary_search(0, n_B - 1, target) == -1:
        result.append(target)

print(len(result))
for i in result:
    print(i, end = " ")