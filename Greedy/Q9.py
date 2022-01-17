s = input()

'''
중복되는 값을 세어줄 cnt 필요
블록의 크기 1 ~ ? -> s의 길이의 반토막만 되도록 len(s) // 2 까지
'''
result = 1001
for i in range(1, len(s) // 2 + 1 ):
    # i가 의미하는것은 자르는 크기
    ago_value = s[:i]
    cnt = 1
    compressed_string = ""

    for j in range(1, len(s) // i):
        now_value = s[i * j:i * (j + 1)]
        if now_value == ago_value:
            cnt += 1
        else:
            if cnt == 1:
                compressed_string += ago_value
                ago_value = now_value
            else:
                compressed_string += str(cnt) + ago_value
                ago_value = now_value
                cnt = 1

    if cnt == 1:
        compressed_string += ago_value
    else:
        compressed_string += str(cnt) + ago_value

    # 분할되고 남은 문자열 추가
    compressed_string += s[i * (j + 1):]

    #print(i,j,compressed_string)
    result = min(result, len(compressed_string))

print(result)

# 해설
def solution_(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j+ step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    
    return answer

print(solution_(s))