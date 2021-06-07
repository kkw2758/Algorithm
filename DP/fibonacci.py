# 동적 계획법을 이용하여 피보나치 수열을 구현해보자.
# 동적 계획법을 사용하지않고 일반적인 방법으로 피보나치 함수를 구현하면 인자값이 커질수록 엄청나게 많은 시간이 소요됨
# 동적 계획법에서 메모이제이션 기법을 사용하여 반복되는 연산을 한번씩만 하게 하여 메모리를 더 잡아먹는 대신에 연산횟수를 확줄이는 방법을 이용


# Top-down - 가장 큰 문제를 방문 후 작은 문제를 호출하여 답을 찾는 방식
# Top-down 으로 구현한 피보나치 함수 n 값은  100이하의 자연수라고 가정.
temp = [0] * 101
def Top_down_fibo(n):
    #print("f({})".format(n), end = " ")
    if n == 1 or n == 2:
        temp[n] = 1
        return temp[n]

    if temp[n]:
        return temp[n]
    
    temp[n] = Top_down_fibo(n - 1) + Top_down_fibo(n - 2)
    return temp[n]

n = int(input())
print(Top_down_fibo(n))


# Bottom-up - 가장 작은 문제들 부터 답을 구해가며 저넻 문제의 답을 찾는 방식
temp = [0] * 101
def Bottom_up_fibo(n):
    temp[1] = 1
    temp[2] = 1

    for i in range(3, n + 1):
        temp[i] = temp[i - 1] + temp[i - 2]

    return temp[n]

print(Bottom_up_fibo(n))