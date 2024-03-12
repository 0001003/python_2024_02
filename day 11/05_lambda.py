# lambda 이름 없는 익명 함수라는 뜻.

def add(x,y):
    return x+y



# 얘를 람다식으로 바꾸면

lambda x,y: x+y



# 두 변수가 들어왔을 때 곱해주는 람다식을 만들어 보세요.
lambda x,y: x*y



# 이 람다식을 어떻게, 왜 쓰냐면

a = 123
b = "123"
c = ['아아','라떼','아바라']
d = lambda x,y: x+y # 변수에다가 함수를 넣는 것이 람다의 일종이라고 보면 됨.

res = d(3,15) # < d라는 변수에 담긴 람다식에 3이랑 15를 넣을 거야. 그걸 res라는 변수에 넣어줘.

# 어떠한 문자를 넣었을 때, 대문자화 시켜주는 람다식을 만들어보자
e = lambda x: x.upper()