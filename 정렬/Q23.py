# 2022/03/07 Baek 10825

import sys
input = sys.stdin.readline

n = int(input())
student_score_list = []

for _ in range(n):
    student_score_list.append(input().split())

student_score_list.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student_score in student_score_list:
    print(student_score[0])

# result = list(map(lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]), student_score_list))
# result.sort()
# for _ in result:
#     print(_)



