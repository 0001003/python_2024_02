# str_adv
# number, str, bool, list
# 문자열 연산자
# + : 연결 연산자
# * : 반복 연산자
# "ice"[0] => "i": 인덱싱 연산자
# "americano"[0:5]: 슬라이싱 연산자
# in : "ice" in 'ice_americano": in 연산자

# print(), input(), int(), str(), bool(), list()
# len() # 길이를 구해줌. [문자] 문자 길이, [리스트] 요소 개수
# a = len(['a', 'b', 'c'])

# test = "americano".replace("cano", "ka")
# print(test)
# b = "사과,바나나,체리".split(',') # 문자 -> 리스트 /
# c = list("사과,바나나,체리")
#
# print(b,c)
#
# d = "사과, 바나나, 체리".split(', ') # << ', '까지, 구분자를 명확하게 넣어줘야 한다
# print(d)
# e = ",".join(['a','b']) #<< join()안에는 []list를 쓴다는 것 리스트>문자열로 변경
# print(e)


# 유저한테 문자 입력을 받고
# 단어 사이에 !를 넣는 프로그램 만들기
# ice -> i!c!e! , ace -> a!c!e

# a = str(input(문자 입력 :)).join('!')
# print(a)

word = input("단어 입력 : ")
result = "!".join(list(word))
print(result)


# is ~~니?
"a".isdigit() #숫자니?
"b".isalnum() # 숫자 or 문자이니?
"c".islower() # 소문자니?
"d".isupper() # 대문자니?

