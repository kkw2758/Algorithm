from bz2 import compress


def solution(s):
    INF = int(1e9)
    answer = INF
    
    for i in range(1, len(s) + 1):
      result = ""
      before = ""
      cnt = 1
      for j in range(len(s) // i):
        now = s[i*j:i*j+i]
        # print("now = {}".format(now))
        if before == now:
          cnt += 1
        else:
          if cnt == 1:
            result += before
          else:
            result += (str(cnt) + before)

          before = now
          cnt = 1

      if cnt != 1:
        result += str(cnt) + before
      else:
        result += before

      result += s[i*j + i:]
      # print(result)
      answer = min(answer, len(result))

    return answer

s = input()
result = solution(s)
print(result)


# def solution(s):
#   answer = len(s)

#   for step in range(1, len(s)//2 + 1):
#     compressed = ""
#     prev = s[0:step]
#     count  = 1

#     for j in range(step, len(s), step):
#       if prev == s[j:j + step]:
#         count += 1
#       else:
#         if count >= 2:
#           compressed += str(count) + prev
#         else:
#           compressed += prev
        
#         prev = s[j:j+ step]
#         count = 1

#     if count >= 2:
#       compressed += str(count) + prev
#     else:
#       compressed += prev

#     answer = min(answer, len(compressed))

#   return answer