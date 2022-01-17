from this import d


score = input()

mid = len(score) // 2

l_sum = 0
r_sum = 0

for x in score[:mid]:
    l_sum += int(x)

for x in score[mid:]:
    r_sum += int(x)

if l_sum == r_sum:
    print("LUCKY")
else:
    print("READY")