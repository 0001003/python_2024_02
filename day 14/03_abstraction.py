# 추상화 >> 구체적인 걸 추상적으로 만드는 것이 추 상 화 ~~

from abc import ABC, abstractmethod
## ^^ Abstract Base Classes의 줄임말.



# 도형 넓이와 둘레를 구하는 프로그램을 만들 것임
# 추상 클래스는, 미리 자식들이 가질 속성과 메소드를 규격화함.
# 어떤 도형을 만들지 모르니까 Shape라는 클래스를 만들어 놓는 것임.
# 프로그래머가 실수하지 말라고 미리 규격화 시켜놓은 것. 추상화.

class Shape(ABC): #ABC가 뭐임?
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def round(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def round(self):
        return 3.14 * self.radius * 2

# triangle, square 클래스 만들고
# circle, triangle, square 각각 인스턴스를 만들고 각각의 넓이와 둘레를 출력하기

class Triangle(Shape):
    def __init__(self, segment, height):
        self.segment = segment
        self.height = height

    def area(self):
        return 1/2 * self.segment * self.height

    def round(self):
        return 3 * self.segment

class Square(Shape):
    def __init__(self, segment):
        self.segment = segment

    def area(self):
        return self.segment * self.segment

    def round(self):
        return 4 * self.segment



a = Circle(5)
b = Triangle(3, 4)
c = Square(5)
print(f" 원 : {a.area()} {a.round()}")
print(f" 정삼각형 : {b.area()} {b.round()}")
print(f" 정사각형 : {c.area()} {c.round()}")
