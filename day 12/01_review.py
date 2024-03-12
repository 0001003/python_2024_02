# 1. 문자열 my_string과 정수 k가 주어질 때
# my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해주세요

# my_string = str(input("문자열 입력 : "))
#
# def solution(my_string,k):
#     for i in my_string:


# 답
# def solution(my_string, k):
#     return my_string * k
#
# result = solution("megastudy",5)
# print(result)


# 2. 정수 배열 numbers와 정수 n이 매개변수로 주어집니다. numbers의 원소를 앞에서부터 하나씩 더하다가
# 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return하는 solution 함수를 작성해 주세요.

# def solution(numbers, n):
#     sum_of_numbers = 0
#     if [i + i for i in numbers.split()]:
#         if sum_of_numbers > n:
#             return sum_of_numbers
#
# a = solution(1 2 3 4 5,5) # 정수 배열이기 때문에 배열로 들어가야 함.
# print(a)

# 답
def solution1(numbers, n):
    sum_of_numbers = 0
    for i in numbers:
        if sum_of_numbers < n:
            sum_of_numbers += i

    return sum_of_numbers

result = solution1([34,5,71,29,100,34],123)
print(result)

# 3. 알파벳으로 이루어진 문자열 myString이 주어집니다. 모든 알파벳을 소문자로 변환하여
# return 하는 solution 함수를 완성해 주세요.

# def solution2(myString):
#     for i in myString:
#         .lower #사용하면 될 듯

def solution2(myString):
    return myString.lower()

res = solution2("BITCOIN")
print(f"{res}")








