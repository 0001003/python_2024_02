# 함수 정의하는 법
# def add(x, y):
#     return x + y
#
#
# def makeApple(x):  # << x만큼 어떠한 것을 줬을 때
#     return ['사과' for i in range(x)]  # << x에 10을 넣었을 때 i는 0~9 그 후에 사과 개수 보기
#
# print(makeApple()) # 어케 나와야 됨?
#
#
# # 함수 정의하는 법 with 매개 변수가 n개일 때
# def make_pizza(*topping_s):  # << 매개변수 앞에 *를 붙이면 매개변수가 n개로 대체됨
#     print("아래와 같은 토핑이 올라감")
#     for i in topping_s:
#         print(f"추가 토핑 : {i}")  # <<*를 붙이면 topping_s가 range 와 비슷한 역할로 바뀐다는 게 킬포
#
#
# make_pizza("치즈", "파인애플", "페퍼로니", "올리브")


# make_upper(words) 소문자가 매개변수로 들어오면 대문자로 출력해주는 함수를 정의해보기

# def make_upper(words):
#     if words.islower #면
#

def make_upper(*words):
    for i in words:  # 이거 왜 for문 들어옴? range화 시키기 위해서.
        print(i.upper())


make_upper("apple", "banana", "kiwi")


# 숫자를 입력 받는데, 숫자가 홀수면 "홀수입니다", 짝수면 "짝수입니다" 출력하는 함수를 만들기

def num1(*x):
    for i in x: # for를 넣어야 하는 이유. for를
        if i % 2 == 1:
            print("홀수입니다")
        else:
            print("짝수입니다")


num1(1, 3, 4)


def odd_even(*numbers):
    for i in numbers:
        if i % 2 == 1:
            print('홀수입니다.')
        else:
            print('짝수입니다.')

odd_even(1,3,4) #함수는 print 이런 거 쓸 필요 없이 함수 이름과 매개변수값 안에 넣고 싶은 값 넣어주면 된다.

