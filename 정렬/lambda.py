# lambda 인자 : 표현식
# 람다는 함수를 "딱 핝 줄만으로 만들게 해주는 친구


def hap(x, y):
    return x + y

result = hap(10,20)
print(result)

print((lambda x,y : x + y)(1,20))