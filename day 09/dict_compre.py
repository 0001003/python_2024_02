# dict_compre [key-value]
# key name : 추상적, 포괄적 이름이 좋다. 강아지 - 요크셔테리어, 포메라니안,... 처럼


coffeeMenu = ['아메리카노', '라떼', '바닐라', '코코아', '민트모카']
coffeePrice = [2.5, 3.3, 3.5, 3, 4]
# 자료 구조상 아예 모르는 애들이기 때문에 엮어줘야 한다.
# 엮는 방법은 zip을 사용하면 됨.

zip(coffeeMenu, coffeePrice)  # zipper 역할.
# starbucks = list(zip(coffeeMenu,coffeePrice))
# print(starbucks)
# megacoffee = dict(zip(coffeeMenu,coffeePrice))
# print(megacoffee)

# key 값이 아메리카노인 경우는 거의 없음. coffeename이라고 쓰는 게 일반적임. key값에는 명사로 포괄적인 걸 써 줘야 함

# for i in zip(coffeeMenu,coffeePrice)
# 1 > for m,p in zip(coffeeMenu,coffeePrice) # 메뉴와 가격을 둘 다 넣어야 하니까 for 뒤에 m,p 두 개를 넣어주는 것임
# 2 > i 대신 딕셔너리를 꺼내서 name에 m, price에 p값을 넣어준다.
# 3 > 그리고 리스트로 감싸주면 된다.
# 4 > 변수 이름 붙여주기

# starbucks = [{'name': m, 'price': p} for m, p in zip(coffeeMenu, coffeePrice)]
#
# travelList = ['후쿠오카', '오사카', '도쿄', '삿포로', '오키나와']
# planePriceList = [30, 40, 45, 50, 40]
#
# tourPrice = [{'name': m, 'price': p} for m, p in zip(travelList, planePriceList)]
# print(tourPrice)


menu = ["americano", "latte", "mint", "hotchoco"]
# [{'name':'americano','wordLen':9}, {'name':'latte','wordLen':5} ... 로 나타내게 만들어보세요

# len을 사용해서 길이를 구하고 싶음. 근데 그렇게 못 하니까 우선 할 수 있는 거 먼저 하자

length = [9, 5, 4, 8]

menuTable = [{'name': m, 'wordLen': l} for m, l in zip(menu, length)]
print(menuTable)

# 답
a = [{'name': i, 'wordLen': len(i)} for i in menu]
print(a)
