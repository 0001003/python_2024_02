# 고등학생 클래스 설계
# 속성 >> 이름 : 학생의 이름, 학년 : 학생의 학년, 수강 과목 : 학생이 수강하는 과목의 인스턴스를 담느 리스트
# 메서드 >> 과목 등록하기 : 새로운 과목을 수강 과목 리스트에 추가합니다, 과목 제거하기 : 수강 과목 리스트에서 특정 과목을 제거합니다.
#       >> 성적 조회하기 : 학생이 수강 중인 모든 과목의 성적을 조회합니다.

# class HighSchoolStudent:
#     def __init__(self, name, age, grade, subjects):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.subjects = []
#
#     def enroll(self, a):
#         self.subjects.append(a)
#
#     def remove(self, a):
#         self.subjects.remove(a)
#
#     def inquiry(self):
#         print(f"모든 성적 조회 : {self.grade}")


# class Subject:
#     def __init__(self, name, mid_grade, final_grade, quiz):
#         self.name = name
#         self.mid_grade = mid_grade
#         self.final_grade = final_grade
#         self.quiz = quiz
#
#     def calculate(self, mid_grade, final_grade, quiz):
#         print(f"최종 성적 : {self.calculate}")


# 답
class Subject:
    def __init__(self, name, mid_grade, final_grade, quiz):  # 4:4:2로 하기
        self.name = name
        self.mid_grade = mid_grade
        self.final_grade = final_grade
        self.quiz = quiz

    def intro(self):
        print(f"{self.name}")

    def calculate(self):
        print(f"과목명 : {self.name}")
        total = self.mid_grade * 0.4 + self.final_grade * 0.4 + self.quiz * 0.2
        if 90 <= total and total <= 100:
            print('A')
        elif 80 <= total and total <= 90:
            print('B')
        elif 70 <= total and total <= 80:
            print('C')
        elif 60 <= total and total <= 70:
            print('D')
        else:
            print('F')

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = []

    def enroll(self):
        name = input("과목 이름 : ")
        mid_grade = int(input("중간 고사 점수 : "))
        final_grade = int(input("기말 고사 점수 : "))
        quiz = int(input("수행 평가 점수 : "))
        self.subjects.append(Subject(name, mid_grade, final_grade, quiz))

    def remove(self, a):
        if len(self.subjects) == 0:
            print("등록된 과목이 없습니다.")
            return
        for index, item in enumerate(self.subjects):
            print(f"{index}.")
            item.intro()
        delete = int(input("삭제할 과목 번호 : "))
        del self.subjects[delete]


    def inquiry(self):
        if len(self.subjects) == 0:
            print("등록된 과목이 없습니다.")
            return

        for i in self.subjects:
            i.calculate()


a = Student('김메가','24','4')
a.enroll()
a.enroll()
a.inquiry()