# # operator(연산자)
# # 토큰[token]
#
# # 산술 연산자 : +,-,*,/,//,**,% [데이터 타입이 숫자일 때]
# # 연결 연산자 : + [데이터 타입이 문자일 때]
# # 반복 연산자 : * [데이터 타입 문자]
# # print("텀블러"*5)
# # 비교 연산자 : >,<, <=, >=, ==(컴퓨터에서의 등호), !=(다르다)
# # 비교 연산자의 결과 타입 : bool
# # print(f"10 > 5 : {10 > 5}")
# # print(f"10 < 5 : {10 < 5}")
# # print(f"10 >= 5 : {10 >= 5}")
# # print(f"10 <= 5 : {10 <= 5}")
# # print(f"10 == 5 : {10 == 5}")
# # print(f"10 != 5 : {10 != 5}")
# # 대입 연산자 : =, +=, -=, *=, /=
# # name = "메가짱"
# # num = 1
# # num = num + 5
# # num += 10       <<num에다가 10을 더해준다는 표시
# # print(num)      << 최종 num의 숫자가 달라진다. num(변수)을 얼마든지 재설정 할 수 있다.
#
# # 논리 연산자 : 대표적인 토큰은 and, or , not이 있다 << 타겟팅은 bool 연산자
# # and [그리고, 교집합] : 모든 조건이 참인 경우만 True
# print(10 > 5 and 5 > 1 and 1 > 0)
# # or [또는, 합집합] : 하나의 조건이 참이면 True
# print(3 > 5 or 4 > 5 or 5 ==5)
# # not : bool 결과를 반대로 바꿔줌
# print(not True) <<false
# print(not bool(0)) << true
#
# print(not (5 > 3) and not (7 > 3))
#
#
# # 멤버쉽 연산자 : in  << 타겟팅은 문자, 결과값 : bool
# print("mega" in "megastudy") << true
# print("mega" not in "megastudy") << false
#
# # 그룹핑 연산자 () << 괄호
# print(3 + 2 + 1 / 3)
#
# # 슬라이싱 연산자 << 타겟팅 문자열
# # 토큰이 [start:end:step] 이렇게 생김
# "megastudy"[0:5]   # << 모든 프로그램의 시작은 0부터 시작. 1 아님
#                    # 나오는 결과값은 megas 01234 (5 전까지 print 결과값이 나옴)
# print("megastudy"[1:5]) #egas
# print("megastudy"[:5])  #megas
# print("megastudy"[0:5:2]) #mgs
# print("megastudy"[::2]) #mgsuy
#
# # 인덱싱 연산자 : 토큰이 [] 이렇게 생김
# print("coffee"[1])  #o
# print("coffee"[2])  #f


# print(not(5 <= 3) or not(3 <=1))
#print(5>3 and 3>1) << 대우