# 1st 유저에게 난이도를 고르게 하기 (쉬움, 보통, 어려움)
# 2nd 난이도에 따라서
#   쉬움 0 ~ 100, 보통 0 ~ 1000, 어려움 0 ~ 10000 랜덤 숫자 뽑기
# 3rd 유저가 입력한 정수가 랜덤 숫자보다 낮으면 down, 높으면 up, 맞추면 정답!
# 4th 기회는 총 6번 안에 계속 맞출 수 있게끔. 넘으면 game over

# level = int(input("난이도(1~3)를 고르시오"))
# 1,2,3 설정 ?
# import random
# 레벨 선택 후
# while level ==1:
#     if
#
# while level ==2:
#     if
#         print("up")
#     elif
#         print("down")
#     else:
#         == n(숫자 맞췄을 때):
#         break  # << while문 1,2,3에 다 넣으면 되지 않나
# while level ==3:

import random

difficulty = int(input("난이도를 고르세요 (1. 쉬움 2. 보통 3. 어려움"))
randomNumber = {
    1: random.randint(0, 101),
    2: random.randint(0, 1001),
    3: random.randint(0, 10001),
}

answer = randomNumber[difficulty]
life = 0

while life < 6:
    user = int(input("정답을 입력하세요: "))
    if answer == user:
        print("정답입니다.")
        break
    else:
        if answer > user :
            print("up")
        else:
            print("down")

    life += 1

if life == 6:
    print("game over")
    print(f"정답은 {answer}입니다.")
else:
    print("승리하셨습니다.")

## 여기서 크게 while문 감싸서 게임 한 번 더 할 거냐는 것까지 만들어보기 yes no해서


