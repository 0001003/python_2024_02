# 정수 분리기 프로그램

# num = int(input("0-99,999 사이의 정수를 입력하세요 : "))

# 다른 one, ten, hundreds... 등 만들고 나눠야 한다는 생각은 했는데
# 이름을 어떻게 붙여야 할 지 모르겠음

# 답
num = int(input("0~99,999 사이의 정수 입력 :")) #87452
ten_thousands = num // 10000 #파이썬 나누기       #8
thousands = (num % 10000) // 1000              #7
hundred = (num % 1000) // 100
ten = (num % 100) // 10
one = num % 10
print(f"{ten_thousands}만 {thousands}천 {hundred}백 {ten}십 {one}")


# 시간 변환기
time = int(input("초 단위 정수 입력 :"))
hour = time // 3600
min = (time % 3600) // 60
sec = time % 60
print(f"{hour}시 {min}분 {sec}초")


# 100의 자리만 뽑기
number = int(input("10000-99999 사이의 정수를 입력 :")) #15745
print(f"{(number // 100} % 10}")

#운동 순서

a = input("운동 입력 :")
b = input("운동 입력 :")
c = input("운동 입력 :")

exercise = []
exercise.append(a)
exercise.append(b)
exercise.append(c)
print(f"{exercise[0]}->{exercise[1]}->{exercise[2]}")
