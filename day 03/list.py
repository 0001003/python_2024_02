# 문자, 숫자, 불리언, !!(리스트)!!
a = "123" #문자
b = 123 #숫자
c = False #불리언
d = [] #리스트

soccer = ["손흥민", "조현우", "조규성", "황희찬"] #리스트
print(soccer) # << 여기서 조현우를 뽑고 싶다
print(soccer[1]) # << 1번 자리에 있는 조현우가 print로 나옴
print(soccer[3]) # << 3번 자리에 있는 황희찬 나옴

# list 안에 어떤 타입이든 들어갈 수 있다
movie = ["웡카", 6000, False, "시민덕희", True]
print(movie[1])
print(not movie[2]) #True
print("시민" in movie[3]) #True

# 리스트화 시켜주는 것
a = list("아이스아메리카노") # << 문자열이 기본, 리스트화 시켜버린다.
print(a)