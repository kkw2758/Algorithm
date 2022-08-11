# def perfect_check(p):
#     left_cnt = 0
#     right_cnt = 0
#     for idx in range(len(p)):
#         if p[idx] == "(":
#             left_cnt += 1
#         else:
#             right_cnt += 1
#         if right_cnt > left_cnt:
#             return False
    
#     return True

# def make_uv(p):
#     left_cnt = 0
#     right_cnt = 0
#     for idx in range(len(p)):
#         if p[idx] == "(":
#             left_cnt += 1
#         else:
#             right_cnt += 1
#         if left_cnt == right_cnt:
#             u = p[:idx + 1]
#             v = p[idx + 1:]
#             return u, v

# def make_u(p):
#     result = ""
#     for idx in range(1,len(p) - 1):
#         if p[idx] == "(":
#             result += ")"
#         else:
#             result += "("

#     return result
    
# def solution(p):
#     if p == "":
#         return ""

#     u, v = make_uv(p)
#     answer = ''
    
#     if perfect_check(u):
#         return u + solution(v)
#     else:
#         answer = ""
#         answer += "("
#         answer += solution(v)
#         answer += ")"
#         answer += make_u(u)
        

#     return answer

# p = input()
# print(solution(p))

def check_perfect_string(string):
    left = 0
    right = 0
    for i in string:
        if i == "(":
            left += 1
        else:
            right += 1
        if right > left:
            return False
    return True

def check_balnaced_string(string):
    left = 0
    right = 0
    for i in string:
        if i == "(":
            left += 1
        else:
            right += 1
    
    if left == right:
        return True
    else:
        return False

def solution(p):
    answer = ""
    if p == "":
        return p
    for i in range(2, len(p) + 1, 2):
        u = p[:i]
        v = p[i:]
        if check_balnaced_string(u):
            if check_perfect_string(u):    
                answer = u + solution(v)
            else:
                answer = "("
                answer += solution(v)
                answer += ")"
                for j in u[1:-1]:
                    if j == "(":
                        answer += ")"
                    else:
                        answer += "("
            return answer

string = input()
print(solution(string))


# def perfect_check(p):
#     left_cnt = 0
#     right_cnt = 0
#     for idx in range(len(p)):
#         if p[idx] == "(":
#             left_cnt += 1
#         else:
#             right_cnt += 1
#         if right_cnt > left_cnt:
#             return False
    
#     return True

# def make_uv(p):
#     left_cnt = 0
#     right_cnt = 0
#     for idx in range(len(p)):
#         if p[idx] == "(":
#             left_cnt += 1
#         else:
#             right_cnt += 1
#         if left_cnt == right_cnt:
#             u = p[:idx + 1]
#             v = p[idx + 1:]
#             return u, v

# def make_u(p):
#     result = ""
#     for idx in range(1,len(p) - 1):
#         if p[idx] == "(":
#             result += ")"
#         else:
#             result += "("

#     return result
    
# def solution(p):
#     if p == "":
#         return ""

#     u, v = make_uv(p)
#     answer = ''
    
#     if perfect_check(u):
#         return u + solution(v)
#     else:
#         answer = ""
#         answer += "("
#         answer += solution(v)
#         answer += ")"
#         answer += make_u(u)
        

#     return answer