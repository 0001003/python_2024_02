# 함수[function]: (마술 상자) [input(None) & output(None)이 있음] None을 넣을 수도, None값이 나올 수도 있음
# [내장(or 파이썬, 표준) 함수] > print(), input(), int(), str(), bool(), len(), sum(), enumerate(), zip()
# [문자열 함수] "abe".upper(), "abe".isUpper(), "acb".count('a')... << 위 아래줄 모두 함수임

# a = str(123)  # 123이 input, a가 문자열 123을 뱉어준다는 뜻.
# b = len("abcde")
#
#
# # 함수를 직접 정의할 수도 있다!
# def add(a, b):
#     c = a + b  # c 없애고 리턴값에 a+b로 바로 넣어도 됨
#     return c
#
#
# k = add(100, 200)
# print(k)
#
#
# # substract, multiply 함수를 만들어보기
#
# def substract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     d = a * b
#     return d
#
# # '🥚' 을 넣으면
# # '🍳' 가 나오게끔. 나머지 나오면 ? 나오게 makeTofry 함수 만들어보기
#
# def makeTofry(🥚,🍳)
#     else print("?")
#     return #어떤 걸 리턴 값에 넣어야 하나?

# def makeTofry(x):
#     if x == '🥚':
#         return '🍳'
#     else:
#         return '??'
#
#
# a = makeTofry('🥚')
# print(a)


# def bank
# 농협은행 > 넘이쁘네, 기업은행 > 귀여운데, 국민은행 > 고민해, 신한은행 > 신나네, 그 외 > ? 나오게 함수 만들기

# def bank(x):
#     #     if x == '농협 은행':
#     #         return '넘이쁘네'
#     #     elif x == '기업 은행':
#     #         return '귀여운데'
#     #     elif x == '국민 은행':
#     #         return '고민해'
#     #     elif x == '신한 은행':
#     #         return '신나네'
#     #     else:
#     #         return '??'
#     #
#     # b = bank('ㅏ')
#     # print(b)
#
#     bankName = {  ##dict 사용해도 됨
#         '농협 은행': '넘이쁘네',
#         '기업 은행': '귀여운데',
#         '국민 은행': '고민해',
#         '신한 은행': '신나네',
#
#     }
#     return bankName.get(x, '?')
# c = bank('k')
# print(c)



# 가변 매개변수 * : n개라는 뜻. 몇 개 추가 될 지 모르니까 *~~ 쓰면 됨
def makePizza(*topping):
    print("피자 굽는 중")
    for i in topping:
        print(f"추가되는 토핑:{i}")

makePizza('치즈','버섯','올리브','페퍼로니') # << 몇 개 추가해도 됨


# zodiac 띠구하기
# def zodiac(*year) [1996 ~ 2005]
# zodiac (1996,2000,2005) > 쥐, 용, 닭

def zodiac(*year):
    zodiacdict = {
            '1996': '쥐',
            '1997': '소',
            '1998': '호랑이',
            '1999': '토끼',
            '2000': '용',
            '2001': '뱀',
            '2002': '말',
            '2003': '양',
            '2004': '원숭이',
            '2005': '닭',
            '2006': '개',
            '2007': '돼지',
    }

    for i in year:
        print(f"{zodiacdict[str(i)]}")

zodiac(1999,2000,2001,2002,2003) ## '1999', '2000'하기 귀찮으니까 108번째 줄 i에 str 씌워버리면 됨


# 자연수 n이 매개변수로 들어오면, 배열화시키고 반대로 나타내기
# 12345 > [5,4,3,2,1]
# 8974 > [4,7,9,8]

def reverse(n): # 배열화를 어떻게 시키지? 반대로 나타내는 건 또 어케함
    # str(n) #"12345"
    # list(str(n)) #"[1,2,3,4,5]"
    numList = list(str(n))
    numList.reverse()
    return [int(i) for i in numList]

print(reverse(12345))




















