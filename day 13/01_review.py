# 1. 정수 n과 k가 주어졌을 때, 1 이상 n 이하의 정수 중에서
# k의 배수를 오름차순으로 저장한 배열을 return하는 solution 함수를 완성해 주세요.

# numList = [i for i in range(1, n+1)]
#
# def sol(n,k):
#     k

# 답

# def solution1(n, k):
#     return [(i+1) * k for i in range(n//k)]
#
# print(solution1(15,5))



# 2. 정수 배열 arr와 자연수 k가 주어집니다. 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면
# arr의 모든 원소에 k를 더합니다. 이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.

# def sol2(arr, k):
#     if k % 2 == 1:
#         return [arr * k]
#     else:
#         return [arr + k]
#
#
# res = sol2([1,2,3,4,5],5)
# print(res)

# 답

# def sol2(arr, k):
#     if k % 2 == 1:
#         return [i * k for i in arr]
#     else:
#         return [i + k for i in arr]
#
# def sol2(arr, k):
#     return [i * k if k % 2 == 1 else i + k for i in arr]

# 3. 주어진 문자열 리스트를 하나의 문자열로 병합하는 함수를 reduce를 사용하여 작성하시오.
# 각 문자열 사이에는 공백을 넣으시오.
# 예시 입력 : ['Python','is','awesome!']
# 예시 출력 : 'Python is awesome!'

from functools import reduce

# list1 = ['Python','is','awesome!']
#
# def merge(acc,cur):
#     return acc+cur.split(" ")
#
# res = list(reduce(merge,list1))
# print(res)

# 답
list1 = ['Python','is','awesome!']

def concat(acc,cur):
    return acc + ' ' + cur

res = reduce(concat,list1)
print(res)

#답
numList = [1,2,3,4,5,6]

def countEven(acc,cur):
    if cur % 2 == 0:
        return acc + 1
    else:
        return acc

res1 = reduce(countEven,numList,0)
print(res1)