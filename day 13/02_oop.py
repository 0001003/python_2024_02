# 변수 -> 문자열, 불리언, 넘버,,, 리스트, 세트,  등등을 데이터 타입이라고 함.
# 정수 타입, 실수 타입, 문자열 타입 포괄할 수 있음 => '나'만의 타입을 만들 수 있다.
# 대학생 타입>>변수 모음[학번, id, 학과, 이름](명사) + 함수 모음[학점 입력, 이름 바꾸기, 전과하기](동사) = 객체>> 대학생[Object]

#object문을 쓸 때는 class를 사용한다.

# 자동차 클래스 만들기 ~~
# car : company, model, year // honk(), intro() << 차에 대한 소개

class Car:
    def __init__(self,company,model,year):
        self.company = company
        self.model = model
        self.year = year

    def honk(self):
        return "빵빵"

    def intro(self):
        return "차에 대한 소개"


# print를 어떻게 해야 함? 아까 쌤이 어케 설명했는지 도저히 이해가 안 됨 지금 ㅋㅋㅋㅋ

class Car:
    def __init__(self,a,b,c):
        self.company = a
        self.model = b
        self.year = c

    def honk(self):
        print("빵빵")

    def honk1(self):
        return "빵빵"

    def intro(self):
        print(f"제작회사 {self.company} , 모델:{self.model}, 연식:{self.year}")

    def intro1(self):
        return f"제작회사 {self.company} , 모델:{self.model}, 연식:{self.year}"


tesla = Car("테슬라","Y-model",2023)
tesla.honk()
print(tesla.honk1())
tesla.intro()
print(tesla.intro1())