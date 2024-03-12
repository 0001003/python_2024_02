# 내장함수
# input,print,int,sum,len,max,min,enumerate(순서까지 뽑는 것),zip

# 오늘은 map, filter, reduce를 배울 건데, 매우매우매우매우 중요~~~~ 핵중요

# map : 치환/변경 해 주는 함수
# map(콜백 함수, 리스트 or 문자열 같은 반복 가능한 것들이 들어감.) < 두 개의 매개변수를 넣는다.
# 앞에는 콜백 함수, 뒤에는 리스트나 문자열
# map(how,what) >> 무엇(what)을 어떻게(how) 바꿔줄까? 로 해석하면 됨

# num = [2,4,6,8,10]
#
# def addTen(x):
#     return x + 10
#
# map(addTen, num) # << map은 오른쪽에 있는 것을 왼쪽에 있는 걸로 치환해주세요~ 라는 뜻임

# ---------------
# map(addTen, num)
# map(addTen(10), num)의 차이는 어떻게 될까?
#
# 밑에를 보렴.


# def one(x):
#     return 1
#
# map(one,num)
# map(one(5),num) >> map(1,num) 애초에 콜백 '함수'를 달라고 했는데 왜 '함수값'을 주는 거야? 에러 바로 떠 버림
# print()<< ()는 앞에 붙은 함수를 실행해 줘~ 라는 뜻. 여기서는 print를 실행해 줘

# # callback 함수 >> 함수 안에 다른 함수를 넣는 것. (합성함수 개념)

# num = [1,2,3,4,5]

# def square(x):
#     return x * x
#
# res = map(square,num)
# print(list(res))

# ----------------------

# def plusTen(x):
#     return x + 10              # >> lambda x : x + 10 이건 고급 문법. 갈수록 코드를 간략하게 추상화, 최적화 시켜야 함.
#
# result = map(plusTen, num)
# print(list(result)) # << list 내장함수를 해 줘야 하는 이유는 map 타입을 list화 해줘야 하기 때문에.
#                     #     1 < int / "1" < str / []이나 list < list 처럼 타입이 다 다른데 얘는 map 타입이라서 맞춰줘야 함.


# 1-100까지 있는 리스트에서 홀수면 +10씩을 해 주고 짝수면 제곱하는 함수 만들기.

# numList = []
#
# def odds_evens():
#     numList = []
#     for i in numList:
#         if i % 2 == 1:
#             return i + 10
#         else:
#             return i * i
#
# res = map.(odds_evens,numList)
# print(res)

#답

# numList = [i for i in range(1,101)]
#
# def sol(x):
#     if x % 2 == 1:
#         return x + 10
#     else:
#         return x ** 2
#
# res = list(map(sol,numList))
# print(res)


# 1-100까지 있는 리스트에 20-30까지는 사과로, 나머지는 숫자 그대로 출력하는 함수 만들기

# numList2 = [i for i in range(1,101)]
#
# def apple(x):
#     if 20 <= x <= 30:
#         return '🍎'
#     else:
#         return numList2
#
# a = list(map(apple,numList2))
# print(a)
#
# # 답
#
# def sol1(x):
#     if 20 <= x and <= 30: # and 없애고 하나로 퉁 쳐도 된다
#         return '🍎'
#     else:
#         return x
#
# res1 = list(map(sol1,numList2))
# print(res1)


fruits = ['pineapple','grapefruit','orange','kiwi','apple','tomato'] #를 대문자로 바꿔주는 함수

# def Upper(x):
#     return fruits.upper
#
# print(list(Upper))

# def sol3(x):
#     return x.upper
#
# res3 = list(map(sol3.fruits)) ##<< 바꿔주세요 sol3 형태로 fruits를.
# print(res3)

# res3 = list(map(lambda x:x.upper(),fruits))로도 가능함.


# 과일에서 알파벳 'o'가 들어가면 대문자화 시켜주고, 안 들어가면 과일글자 길이로 바꿔주는 함수 만들기

def fruit(x):
    if 'o' in x:
        return x.upper()
    else:
        return len(x)

f = list(map(fruit,fruits))
print(f)
