# map : 치환 / filter : 거름 / reduce : 누적
# reduce는 누적이다

from functools import reduce
#
# # reduce는 how랑 what 똑같이 들어감. !!!!!! reduce는 매개변수 2개를 요구함
#
# numlist = [1,2,3,4]
# def sol(acc,cur): # acc 누적하다, cur 위치에는 현재
#     print(f"acc:{acc}, cur:{cur}")
#     return acc+cur
#
#
# res = reduce(sol,numlist)
# print(res)

# 1-1000까지의 누적합을 구해보세요

numList = [i for i in range(1,1001)]

def sol1(acc,cur):
    return acc+cur

res1 = reduce(sol1,numList)
print(res1)