# 2022/11/17 baek_1654

K, N = map(int, input().split())

lans = []
for _ in range(K):
    lan = int(input())
    lans.append(lan)

result = 0
def parametric_search(start, end):
    global result
    while start <= end:
        mid = (start + end) // 2
        
        lan_cnt = 0
        for i in range(K):
            lan_cnt += lans[i] // mid
        # 자른 렌선이 필요보다 많으면? - 더길게 자름
        if lan_cnt >= N:
            result = mid
            start = mid + 1
        # 자른 렌선이 필요보다 적으면 - 더 짧게 자름
        else:
            end = mid - 1
    
parametric_search(1, max(lans))
print(result)