# dict
#  key-value, key(고유, only-one)
# key : int, str 형만 가능
# value : 다 됨 (하고 싶은 거 다 해 ~)

issac = {
    'ham': 2500,
    'cheese': 3000,
    'bacon': 3000,
    # 왼쪽은 key 값, 오른쪽은 value 값 // 이것도 쉼표 마지막에 써야 함
}

print(f"{issac}")
print(f"{issac['ham']}") #2500




bong = {

    'eggham': 3800,
    'soya': 3200,
    'original': 3000,

}

print(f"{bong}")

cgv = {

    'popcorn':['소금', '카라멜', '어니언'],
    'beverage':{
        'sprite':2000,
        'zero_coke':1500,
    }

    }
print(f"{cgv['popcorn'][0]}") #소금
# 제로콜라 가격 빼 오기
print(f"{cgv['beverage']['zero_coke']}")


mbti = {
    'e':'외향적',
    'i':'내향적',
    's':'현실적',
    'n':'미래지향적',
    'f':'감성적',
    't':'이성적',
    'p':'즉흥적',
    'j':'계획적',


}

# users_mbti = str(input("당신의 mbti를 입력하세요 :"))
# print(f"당신은 {mbti})

users_mbti = input("당신의 mbti를 입력하세요 :") #entj
print(f"당신은 {mbti[users_mbti[0]]} {mbti[users_mbti[1]]} {mbti[users_mbti[2]]} {mbti[users_mbti[3]]}")

