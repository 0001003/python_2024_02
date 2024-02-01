# type_change
# 숫자 / 문자 / 불린형 타입이 있는데 타입을 변경해 볼 것임!

#print() 출력, input() 입력
#int() 정수화, float() 실수화
#str() 문자화, bool() 불린화

# a = "123"
# num_a = int(a)
# b = "456"
# num_b = int(b)
# print(f"{a+b} , {num_a+num_b}")

# QUIZ
# a = input("첫 번째 숫자 입력:")
# b = input("두 번째 숫자 입력:")
# print("결과:") << 내보기

# num_a = int(a)
# num_b = int(b)
# print(f"결과: {num_a+num_b}")

# a = int(input("첫 번째 숫자 입력:"))
# b = int(input("두 번째 숫자 입력:"))
# print(f"결과: {a+b}")

c = str(123)
d = str(123)
print(f"결과: {c + d}")

num = int(3.14)
print(num) # << 실수 부분에서 정수화를 씌워버리면 정수만 남게 된다.