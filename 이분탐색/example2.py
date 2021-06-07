'''
<떡볶이 떡 만들기>
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다.
동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기에 높이 (H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19,14,10,17 cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15,14,10,15cm이 될 것이다.
잘린 떡의 길이는 차례대로 4,0,0,2cm이다. 손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

입력조건
첫째 줄에 떠그이 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
둘째 줄에는 떡의 개별 높이가 주어지낟. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

출력조건
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
'''



n, m = map(int,input().split())
array = list(map(int, input().split()))

min_value = min(array)
max_value = max(array)

h = 0


# binary_search(min_value, max_value)
def binary_search(start, end, array):
    global h
    if start > end:
        return

    mid = (start + end) // 2
    
    sum = 0
    for member in array:
        if member - mid > 0:
            sum = sum + member - mid
    if sum == m:
        h = mid
        return
    elif sum > m:   # 자른 떡의 길이가 손님이 요구한 떡보다 길면?
        h = max(h , mid)
        binary_search(mid + 1, end, array)
    else:
        binary_search(start, mid - 1, array)


binary_search(min_value, max_value, array)
print(h)


n, m = map(int,input().split())
array = list(map(int, input().split()))

start = min(array)
end = max(array)

result = 0

while start <= end:
    mid = (start + end) // 2

    total = 0
    for x in array:
        if x > mid:
            total = total + x - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)