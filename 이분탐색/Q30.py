from bisect import bisect_left, bisect_right

def count_by_range(target, left_value, right_value):
  right_index = bisect_right(target, right_value)
  left_index = bisect_left(target, left_value)
  return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
  answer = []
  for word in words:
    array[len(word)].append(word)
    reversed_array[len(word)].append(word[::-1])

  for i in range(10001):
    array[i].sort()
    reversed_array[i].sort()

  for q in queries:
    if q[0] == "?":
      res = count_by_range(reversed_array[len(q)], q[::-1].replace("?","a"), q[::-1].replace("?","z"))
    else:
      res = count_by_range(array[len(q)], q.replace("?","a"), q.replace("?","z"))

    answer.append(res)

  return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))