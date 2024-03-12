# 조건에 맞게 수열 변환하기
# 정수 배열 arr와 자연수 k가 주어진다. 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고,
# k가 짝수라면 arr의 모든 원소에 k를 더한다. 이러한 변환을 마친 후의 arr를 return하는 solution 함수 만들기.

# k = int(input("자연수 1개 입력 : "))
# arr = [1,2,3,100,99,98]     # list랑 정수는 자료형이 맞지 않아서 연산이 안 된다.
#
#
# def solution(k):
#     if k % 2 == 1 :
#         print(f"{arr}*{k}")
#     else :
#         print(f"{arr}+{k}")
#
# return

# 함수 정의하는 법
# def abc(x): << x가 문자열 '1'인지, 숫자 1인지, bool인지 모른다.
#               파이썬의 치명적인 단점 / x와 y의 위치가 바뀌면 안된다.
# return x + 10 << x에 +10을 하는 함수값을 돌려줄게.

def solution(arr, k):  # << 미지수(x,y)라고 생각하면 됨. 3개 4개... ()안에 들어가는 개수 더 커질 수 있음.
    if k % 2 == 1:
        newList = []
        for i in arr:
            newList.append(i * k)
        return newList
    else:
        newList = []
        for i in arr:
            newList.append(i + k)
        return newList


# al = [1, 2, 3, 4, 5]
#
# [i * 10 for i in al] << i는 al 안에 있는 애들인데 거기에 i * 10을 해줘라는 뜻.

# 단축버전
def solution(arr, k):
    if k % 2 == 1:
        return [i * k for i in arr]
    else:
        return [i + k for i in arr]


# 더 단축 버전
def solution(arr, k):
    return [i * k if k % 2 == 1 else i + k for i in arr]
    # << if 기준으로 참이라면 왼쪽에 있는 i*k를 보여주고, 그게 아니라면 i + k를 보여줘.


# 제일 작은 수 제거하기
# 정수를 저장한 배열, arr에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를 들어 arr이 [4,3,2,1]인 경우는
# [4,3,2]를 리턴하고, [10]이면 [-1]을 리턴합니다. << 10은 리스트 안에 한 개 밖에 없으니까 빈 배열로 처리해서 -1이 나오는 것.

def min_remove(arr, x):  # << 왜 x는 또 안 들어옴
    if min(arr):


def removeMinArr(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.sort #<array를 정렬하면 작은수~큰 수로 정렬이 된다.
        return arr[1:len(arr)]


# 파이썬에서 내장함수 사용.
# len([1,2,3,4,5,6])< 길이가 6이니까 6을 돌려줌, sum([1,2,3,4,5]) < 합을 돌려줌
# max([1,2,3,4,5,6])< 제일 큰 수가 6이니까 6을 돌려줌, min([1,2,3,4,5]) < 제일 작은 수가 1이니까 1을 돌려줌

def removeMinArr(arr):
    if len(arr) == 1:
        return [-1]
    else:
        minimum = min(arr)
        arr.remove(minimum)
        return arr
