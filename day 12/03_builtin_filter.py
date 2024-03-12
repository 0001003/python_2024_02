# filter - 걸러주는 것.
# filter(콜백함수, 타겟팅)
# filter(how,what)
# 콜백함수의 결과값이 boolean 값으로 나와야 한다.

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sol1(x):
    return x >= 5   ## true 나 false로 나와야 한다.

res1 = list(filter(sol1,numList))
print(res1)



# 3의 배수를 람다함수 써서 걸러주세요~ filter 사용
lambda x : x % 3 == 0

res2 = list(filter(lambda x : x % 3 == 0, numList))
print(res2)


# 첫번째 글자가 a이거나 마지막 글자가 y인 애들만 필터링 하기
fruits = ['apple','banana','cherry','kiwi','avocado','strawberry']

# def filter1(x):
#     if x in 'a'[0] and 'y'[-1]:
#         return x
#
# res3 = list(filter(filter1,fruits))
# print(res3)

def sol2(x):
    return x[0] == 'a' or x[-1] == 'y'

res2 = list(filter(sol2,fruits))
# res2 = list(filter(lambda x: x[0] == 'a' or x[-1] == 'y', fruits)) << 람다로도 가능
print(res2)

# 5글자 이하이고 'a'가 포함된 애들만 필터링해줘~

# def sol3(x):
#     return len(x) <= 5 and x in 'a'

# lambda x : len(x) <= 5 and x in 'a'
#
# res3 = list(filter(lambda x : len(x) <= 5 and x in 'a',fruits))
# print(res3)

# 답
# res3 = list(filter(lambda x : len(x) <= 5 and 'a' in x,fruits))
# print(res3)


# 6글자 이상인 애만 걸러주고, 걔네를 대문자화 시켜주세요

res4 = list(map(lambda x: x.upper(),filter(lambda x : len(x) >= 6,fruits)))
print(res4)











