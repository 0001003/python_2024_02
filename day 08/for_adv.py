# fruits = ["자몽", "망고", "블루베리","수박"]
#
# for i in fruits:
#     print(i)
    #자몽
    #망고
    #블루베리
    #수박

## enumerate(): 몇 번째인지(i), 요소(j) 출력 반드시 변수 두 개가 들어가야 함
# for i,j in enumerate(fruits):
#     print(f"{i}번째 {j}")

# ---------------------------------------------------------------------
# fruits = ["apple", "banana", "watermelon", "mango", "blueberry"]
# #알파벳 a가 포함 되어있지 않는 과일이 몇 번째인지 보여주세요
#
# # for i,j in enumerate(fruits):
# #     if not j.count("a") > 0:
# #         print(i)
# #     # if j.count("a") == 0:
# #     #     print(i) << 도 가능하다


# numList = []
# for i in range(11):
#     numList.append(i)

# 리스트 컴프리헨션
# [i for i in range()]
# a = [i for i in range()] #<< a가 변수
# b = [i + 10 for i in range(11)]
#
# # 0부터 10까지의 각각 제곱숫자가 나오게 만들어보기
# c = [i ** 2 for i in range(11)]

fruits = ["apple", "banana", "watermelon", "mango", "blueberry"]
# 대문자화 시켜서 리스트로 만들어보기

d = [i.upper() for i in fruits]
print(d)