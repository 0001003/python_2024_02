# lexical - 어휘라는 뜻을 가지고 있음.

# 함수를 한 번 사용하게 되면 사라짐. 컴퓨터 메모리를 효율적으로 사용하기 위해서.
# 함수 안에서 정의된 변수는 바깥으로 못 나감. 로컬 변수. 지역변수이다.

mega = "ice" # global variable << 전역변수

def abc():
    mega = "123" # local variable << 지역변수
    return mega

def xyz():
    print(mega)
xyz() #<< 함수를 꼭 이렇게 써 줘야지 ice 하고 나온다.