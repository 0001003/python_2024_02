# 반복문 : for, while
# break문 : 반복문 탈출 예약어


# a = 1
# while a < 5:
#     print("파이썬")
#     a += 1

# while True:
#     num = int(input("정수 0을 넣으면 끝남 :"))
#     if num == 0:
#         break

# while문을 사용해서 1~10까지 더한 값을 출력하는 코드 만들기

# a = 1
# a = 1
# total = 0
# while a < 11:
#     total += a
#     a += 1
#  print(total)

# 유저에게 어떤 정수 n을 입력 받고,
# while 무한 루프에서 정수 n을 입력 받으면 탈출하는 코드 만들기

# n = int(input("정수 입력 :"))
# while True:
#     if n==n:
#         break

# n = int(input("정수 입력 :"))
# while True:
#     m = int(input("루프 안에서 정수 입력 :"))
#     if n == m:
#         break

# 랜덤으로 0~10까지 아무 숫자를 뽑고 유저에게 해당 숫자를 맞추게 하는 게임
# 맞추면 정답입니다 하고 끝 틀리면 틀렸습니다 다시 입력하세요. 맞출 때까지

# n = int(input("0~10까지 정수 입력 :"))
# while True:
#     m = int(input("정수 입력 :"))
#     if n == m:
#         print("정답입니다")
#         break
#     else:
#         print("틀렸습니다. 다시 입력하세요")


# 답
import random
answer = random.randint(0,11)
while True:
    a = int(input("정수 입력 :"))
    if answer == a:
        print("정답입니다")
        break
    else:
        print("틀렸습니다. 다시 입력하세요")
