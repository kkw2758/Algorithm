import sys

def is_palindrome(str_):
    left = 0
    right = len(str_) - 1
    while left < right:
        # 1. left right 문자가 동일한 경우:  left + 1, right + 1
        if str_[left] == str_[right]:
            left += 1
            right -= 1
        else:
            # 2. left right 다른 경우: 한 문자열 제거 후 회문 확인
            # 2-1. 오른쪽 문자열 제거한 경우 제거 후 회문이되는지 확인 
            if left < right - 1:
                temp = str_[:right] + str_[right + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            # 2-2. 왼쪽 문자열 제거한 경우 제거 후 회문이되는지 확인 
            if left + 1 < right:
                temp = str_[:left] + str_[left + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            # # 2-3. 회문이 안된 경우, 2리턴  
            return 2
        
    return 0

for _ in range(int(sys.stdin.readline())):
    print(is_palindrome(sys.stdin.readline().strip()))