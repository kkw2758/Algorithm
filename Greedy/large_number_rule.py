# 큰 수의 법칙
# 나의 코드


def large_num_rule(array , m, k):
    array.sort()
    cnt = 0
    result = 0
    for i in range(m):
        if cnt < k:
            result += array[-1]
            cnt += 1
        else:
            result += array[-2]
            cnt = 0

    return result

n, m, k = map(int,input().split())
array = list(map(int,input().split()))

print(large_num_rule(array, m, k))



n, m, k = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
first = array[n-1]
second = array[n-2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break    
        result += first
        m -= 1
        print("Result = {}\nm = {}".format(result, m))

    if m == 0:
        break

    result += second
    m -= 1
    
print(result)



n, m, k = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
first = array[n-1]
second = array[n-2]
result = 0

count = (m//(k + 1)) * k + m % (k + 1)
result += count * first
result += (m - count) * second
print(result)