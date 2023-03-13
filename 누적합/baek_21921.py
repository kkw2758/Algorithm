# 2023/03/10 Baek 21921

import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visit_cnt_list = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    visit_cnt_list[i] += visit_cnt_list[i - 1]

result_list = []
for i in range(X, N + 1):
    result_list.append(visit_cnt_list[i] - visit_cnt_list[i - X])

max_value = max(result_list)
if max_value == 0:
    print("SAD")
else:
    print(max_value)
    print(result_list.count(max_value))
