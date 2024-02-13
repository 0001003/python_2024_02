# 1. 0~100까지의 짝수를 출력하기

# 2. 유저에게 정수를 입력 받고, 해당 정수의 구구단 출력하기
#   3 > 3*3 = 9

# 3. 랜덤으로 0~10000까지의 숫자를 뽑아서 10개를 리스트에 넣고
#    오름차순으로 입력하고, 각 요소의 총합을 구하기

# 1.
# num = int(input("짝수 입력 (0~100) : "))
# for i in range(100):
#     print()
# if (num % 2 == 1)
#     print()
# else ()
# (num % 2 == 0)  # 어느 곳에 배치해야 할 지
# print()

for i in range(101):

    if i % 2 ==0:
        print(i)


# 2.
# num1 = int(input("정수 입력 :"))
# for

num = int(input("정수 입력 :"))
for i in range(1,10):
    print(f"{num}*{i}= {num*i}")


# 3.
import random

numList = []
for i in range(10):
    numList.append(random.randint(0,10001))
numList.sort()
print(numList)

total = 0
for i in numList:
    total += i
print(total)

#위에 거 아니면 내장함수 sum 사용해도 된다
# print(sum(numList))