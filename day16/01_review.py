# 파이썬 복습 퀴즈


# 1. 배열 원소 삭제하기
# 정수 배열 arr과 delete_list가 있습니다. arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은
# 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return하는 solution 함수를 작성해주세요.
# arr = [293,1000,395,678,94] / delete_list = [94,777,104,1000,1,12] / result = [293,395,678]

# def solution(arr, delete_list):
#     if arr - delete_list:
#         print(arr)

# 답
# filter 사용해야 함. 걸러주는 거니까.

# arr = [293,1000,395,678,94] / delete_list = [94,777,104,1000,1,12]
# def solution(arr, delete_list):
#     return list(filter(lambda x: x not in delete_list, arr))

# 차집합 사용하게 되면
a = set([293, 1000, 395, 678, 94])
b = set([94, 777, 104, 1000, 1, 12])
c = list(a.difference(b))
c.sort()
print(c)

# 2. 자연수 뒤집어서 배열 만들기
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를 들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

def solution(n):
    return list(reversed(n))


res = solution(12345)
print(12345)


# 답
def solution1(n):
    listNumber = list(str(n))
    listNumber.reverse()
    return list(map(lambda x: int(x), listNumber))


def solution2(n):
    return list(map(lambda x: int(x), reversed(str(n))))


# 12345
# "12345" str(n)
# "54321" reversed(str(n))
# 5,4,3,2,1  map(lambda x: int(x), reversed(str(n)))
# [5, 4, 3, 2, 1]  list(map(lambda x: int(x), reversed(str(n))))

# 숫자 타입을 역으로 reversed를 못하기 때문에 str 처리를 해 준 뒤에 int(x)를 map해서 합성함수처럼 사용해 준다.
# 그 뒤에 list화, 즉 배열로 답을 내라고 했으니까 list화를 시켜주면 된다.


# 3. 최댓값 구하기
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을
# return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    numbers = []
    for i in numbers:
        return max(i * i)


# 답
a = [1, 2, -3, 4, -5]  # result = 15
b = [0, -31, 24, 10, 1, 9]  # result = 240
c = [10, 20, 30, 5, 5, 20, 5]  # result = 600
a.sort()
b.sort()
c.sort()
print(a, b, c) # << 경우의 수를 생각을 해야 하는 문제임

# max 내장 함수
# max(1,6) >> 6
# max(6,22) >> 22 크기 비교 후 알아서 더 큰 애를 뽑아줌.

def solution3(num):
    num.sort()
    return max(num[0] * num[1], num[-1] * num[-2])
