# first = int(input(f"첫 번쨰 정수 :"))
# second = int(input(f"두 번째 정수 :"))
#
# print(f"두 수의 곱은 {first*second}")

# 1. 태어난 년도 입력하고 현재 만나이 출력
# 2. 세 개의 숫자 평균 계산기
# 3. 정사각형 넓이 계산 프로그램
# 4. 체온 변환기 섭씨 온도 > 화씨 온도
# 5. 체질량 지수 계산기

# 1. 만 나이 계산기

# birth = int(input("태어난 년도"))
# print(f"당신의 만 나이는 {2024-birth}살 입니다.")



# 2. 세 개의 숫자 평균 계산기

# first = int(input("첫 번째 숫자 입력 :"))
# second = int(input("두 번쨰 숫자 입력 :"))
# third = int(input("세 번째 숫자 입력 :"))
#
# print(f"세 숫자의 평균은 {int(first+second+third)/3}입니다.")

# +) avg = (first + second + third)
#    print("f"세 수의 평균은 {avg:.2f}입니다.)   <<.2f >> 소수 둘째 자리까지



# 3. 정사각형 넓이 계산 프로그램

# side = int(input("한 변의 길이 입력 :"))
# print(f"한 변의 길이가 {side}인 정사각형의 넓이는 {side*side}입니다.") ##제곱 표시 side**2


 # 4. 온도 변환기
# degree = float(input("현재 섭씨 온도를 입력 : "))
# print(f"현재 화씨 온도는 {degree*5.9+32}입니다.")


# 5. 체질량 지수 계산기
height = float(input("당신의 키 입력 : "))
weight = float(input("당신의 몸무게 입력 : "))
print(f"당신의 BMI 지수는 {weight/height*height}")
