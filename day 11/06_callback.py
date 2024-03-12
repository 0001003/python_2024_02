# # callback
#
# # 함수를 정의할 때
# # def test(x):
# #     x에다가 함수를 넣을 수 있다.
#
# def test(x):
#     print("함수 시작")
#     x() # 이 함수가 make_fry 함수로 바뀌는 것. 함수가 들어와야 하는데 1값이 들어와서 이 함수는 틀리게 됨.
#     print("함수 끝")
#
# def make_fry(): #매개변수 필요 없으니까 그냥 ()만 함
#     print("🍳")
#     return 1 #print 후라이를 하고 1 값을 돌려주는 함수.
#
#
# test(make_fry) # make_fry를 매개변수로 전달할게
# test(make_fry()) # make_fry()함수를 실행시켜줘> 그것의 결과값이 1 그럼 test 값에 1이 매개변수로 나타난다.
#
# # callback << 함수를 전달을 할게. 그 안에 전달한 함수를 실행시켜줘.
# # 따라서 make_fry가 콜백함수이다.
#
# # 맞는 함수를 만들려면
# def test(cook): # << x자리에 cook를 넣은 것 왜냐면 우리는 음식을 만들고 있으니까
#     print("함수 시작")
#     cook()
#     print("함수 끝")
#
# def make_fry():
#     print("🍳")
#
#
# # 다시 다시. << 사실 f(g(x))처럼 합성함수라고 생각하면 된다. 합성함수는 g(x)값에 따라서 결괏값이 유연해지니까.
#
# def make_rice():
#     print("🍚")
#
# def make_ramen():
#     print("🍜")


# 함수 이름을 pick_fruit(x) x자리에 callback함수를 넣어주고, 함수를 실행시킨 뒤 결과값을 받고 ( res = x() )
# res = x() ["🍎","🍌","🍉"]
# print("{res} 과일을 얻었습니다.") 나오게끔 함수를 만들어 보세요.

def pick_fruit(x):
    res = x()
    print(f"{res} 과일을 얻었습니다.")


a = lambda : "🍎" #
b = lambda : "🍌"
c = lambda : "🍉"

pick_fruit(a)



# 혹은

def apple():
    return "🍎" # >> lambda : "🍎"

def banana():
    return "🍌"

def watermelon():
    return "🍉"

pick_fruit(apple)
