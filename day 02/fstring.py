# fstring
money = "10000"

# variable - 변수[기억하는 곳]
# 변수 이름 짓는 문법
# 1. 영어, 숫자, 특수문자(_)만 사용하기
# 2. 대소문자를 구별함 ex> A, a 다름. Meal, meal 다름
# 3. 띄어쓰기 안 됨 ex> my name 안 됨 -> my_name or myName
# 4. 숫자로 시작 불가능 ex> 1a 안 됨 a1은 됨

# 변수 이름 짓는 국룰
# 1. 변수명은 의미 있는 것으로 짓기
# 2. 두 단어 모여서 이름 지을 때
#   - 1) camelCase -> megaStudy : 뒤 단어 첫 글자 대문자로 해야 함
#        ex) megaCoffee, myAge, yourName
#   - 2) snakeCase -> mega_study, my_age, your_name
# 3. 소문자로 시작

my_age = "21"
myAge = 21
    # << jeon 자체가 변수이기 때문에
myName = "jeon"     # << 쌍따옴표 안에 쓰면 가능함 / 아니면 jeon = "전수효" 처럼 변수 값을 지정을 해 줘야 함


my_name = input("당신의 이름은:")
print(f"안녕하세요 저의 이름은 {my_name}입니다.")