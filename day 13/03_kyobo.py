# Book 클래스 만들기 ~~
# 변수는 제목, 작가, 가격 / 함수는 intro() << 안에 print 넣는 형식으로 만들어보기

class Book:
    def __init__(self,a,b,c):
        self.name = a
        self.author = b
        self.price = c

    def intro(self):
        print(f"책 이름 : {self.name}, 작가 : {self.author}, 가격 : {self.price}")



# 지점(branch)이랑 booklist가 변수인 Bookstore 클래스를 만들어보자.

class BookStore:
    def __init__(self,a):
        self.branch = a
        self.booklist = []

    def bring_in(self,a):
        self.booklist.append(a)


    def showBookList(self):
        print(f"{self.branch}의 책 보유 현황")
        for i in self.booklist:
            i.intro()


shinchon = BookStore("교보 신촌점")
shinchon.bring_in(Book('집에 가고 싶다', '김해인', 50000))
shinchon.bring_in(Book('진심 그만하고 싶다', '이성ㅎ싀', 40000))
shinchon.showBookList()