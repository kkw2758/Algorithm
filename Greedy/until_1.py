'''
def until_1(n, k):
    count = 0
    while n != 1:
        if n % k == 0:
            n = n // k
            count += 1
        else:
            n = n -1
            count += 1

    return count

n, k = map(int, input().split())
print(until_1(n, k))
'''
def upgrade_until_1(n , k):
    count = 0
	# n이 k보다 작으면 '%'연산을 실행할 필요가 없다.
    while n >= k:
        count += n % k
        n = n // k
        count += 1 #n = n//k 연산을 실행했으므로 수행횟수 + 1
    
    #n이 1이 될때까지 빼야하는 수를 수행횟수에 더해준다.
    count += (n - 1)

    return count

n, k = map(int, input().split())
print(upgrade_until_1(n, k))