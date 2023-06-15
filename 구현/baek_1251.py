# 2023/06/16 Baek 1251

word = input()
word_list = []

n = len(word)
for i in range(1, n - 1):
    for j in range(i + 1, n):
        first = word[:i]
        second = word[i:j]
        third = word[j:]
        word_list.append(first[::-1] + second[::-1] + third[::-1])
        
word_list.sort()
print(word_list[0])