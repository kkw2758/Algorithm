# 2023/04/18 WACU컵 6번

N = int(input())
candidates = input().split()

result_set = set()
for i in range(N):
    if candidates[i][-6:] == "Cheese":
        result_set.add(candidates[i])

if len(result_set) >= 4:
    print("yummy")
else:
    print("sad")