# # control_statement(제어문)
# #
#
# # if 조건
#
# # num = int(input("정수 입력:"))
# #
# # if num > 0:
# #     print("양수입니다.")
# # print('프로그램 끝')
#
#
# # 유저에게 문자를 입력 받고, 문자 길이가 10글자 이상이면 너무 길어요!, 프로그램 끝이라는 코드 만들기
#
# # word = str(input("문자 입력 :"))
# #
# # if word
#
# # 답
#
# # word = input("문자 입력 :")
# # if len(word) >= 10:
# #     print("너무 길어요")
# # print("프로그램 끝")
#
# # 유저에게 문자를 입력 받고, 5글자 이상이면서 마지막 문자가 대문자면 통과! 프로그램 끝
#
# # word = input("문자 입력 :")
# # if len(word) >= 5:
# #
#
# # word = input("문자 입력 :")
# # if len(word) >= 5 and word[len(word)-1].isupper():     #  << word[-1].isupper() 이렇게 해도 됨!
# #     print("너무 길어요")
# # print("프로그램 끝")
#
# # num = int(input("정수 입력:"))
# # if num > 0:
# #     print("양수입니다.")
# # else:
# #     print("음수 또는 0입니다.")
# # print("끝")
#
# # # 수를 입력하고 홀수인지 짝수인지 구분하는 프로그램
# # num = int(input("숫자 입력 :"))
# # if num
# #     #나머지 1,0인 애들로 나눠서 print 사용해서 홀수/짝수 구분
#
# # 답
# num = int(input("정수 입력:"))
# if num % 2 == 0:
#     print("짝수입니다.")
# else:
#     printf("홀수입니다.")
#
#
#
# # # 알파벳을 입력하고 알파벳 길이가 홀수인지 짝수인지 구분하는 프로그램
# # word = str(input("알파벳 입력 :"))
# # if (len(word))//2 == 0
# #     print("짝수입니다")
# # else:
# #     print("홀수입니다")
#
# #답
# word = input("단어 입력 :")
# if len(word) % 2 ==0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")
#
#
#
#
# # # 알파벳 하나 입력 했을 때, 대문자인지 소문자인지 구분하는 프로그램
# # word1 = str(input("알파벳 입력 :"))
# # if
#
# # 답
# a = input("알파벳 입력:")
# if a.isupper():
#     print('대문자입니다.')
# else:
#     print('소문자입니다.')

# num = int(input("정수 입력 :"))
#
# if num > 0:
#     print('양수입니다.')
# elif num == 0:
#     print('0입니다.')
# else:
#     print('음수입니다.')

# math = int(input("수학 점수 입력 :"))
#
# if math >= 90 :
#     print('A입니다.')
# elif math >= 80 :
#     print('B입니다.')
# elif math >= 70 :
#     print('C입니다.')
# else:
#     print('샷건을 칩니다.')



# 각0~180도 사이의 각을 입력 받고
# 90도 보다 작으면 예각, 90도면 직각, 90-179 둔각, 180 평각

angle = int(input("각도 입력 : "))

if angle < 90 :
    print("예각")
elif angle == 90 :
    print("직각")
elif angle > 90 and angle <= 179 :
    print("둔각")
else:
    print("평각")

# 답
if 0 < angle and angle < 90:
    print("예각")
elif angle == 90:
    print("직각")
elif 90 < angle and angle < 180:
    print("둔각")
else:
    print("각 입력 오류")

if True: #<< if 안에 if를 쓸 수 있다. 중첩 if문이라고 한다.
    if True:
        print('실행')
    else:
        print('안됨')
else:
    print('안됨')

# 단어를 입력 받고 단어 길이가 홀수 / 짝수 구분해주고
# 단어에 'a'가 포함 되어 있으면 'a'를 포함한 홀수 / 짝수
# 단어에 'a'가 포함 되어 있지 않으면 홀수 / 짝수 출력하는 프로그램

# word = str(input("단어 입력 :"))
#
# if len(word) // 2

word = input("단어 입력 :")

if len(word) % 2 == 0:
    if word.count('a') > 0:
        print('a를 포함한 짝수 입니다.')
    else:
        print('짝수입니다.')
else:
    if word.count('a') > 0:
        print('a를 포함한 홀수 입니다.')
    else:
        print('홀수입니다.')
        