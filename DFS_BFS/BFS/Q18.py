def perfect_check(p):
    left_cnt = 0
    right_cnt = 0
    for idx in range(len(p)):
        if p[idx] == "(":
            left_cnt += 1
        else:
            right_cnt += 1
        if right_cnt > left_cnt:
            return False
    
    return True

def make_uv(p):
    left_cnt = 0
    right_cnt = 0
    for idx in range(len(p)):
        if p[idx] == "(":
            left_cnt += 1
        else:
            right_cnt += 1
        if left_cnt == right_cnt:
            u = p[:idx + 1]
            v = p[idx + 1:]
            return u, v

def make_u(p):
    result = ""
    for idx in range(1,len(p) - 1):
        if p[idx] == "(":
            result += ")"
        else:
            result += "("

    return result
    
def solution(p):
    if p == "":
        return ""

    u, v = make_uv(p)
    answer = ''
    
    if perfect_check(u):
        return u + solution(v)
    else:
        answer = ""
        answer += "("
        answer += solution(v)
        answer += ")"
        answer += make_u(u)
        

    return answer

p = input()
print(solution(p))