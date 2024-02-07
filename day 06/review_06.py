# 영화 예매 프로그램 [dict] 사용

# 사용자로부터 영화 종류와
megaMovie = {
    'movie': {
        'names': ['액션 영화', '로맨스 코미디', '공포 영화'],
        'price': [10000, 8000, 9000],
    },

    'movie1': [
        {'name': '액션 영화', 'price': 10000},
        {'name': '로맨틱 코미디', 'price': 8000},
        {'name': '공포 영화', 'price': 9000},

    ],

    'popcorn': {
        'names': ['치즈 팝콘', '카라멜 팝콘', '일반 팝콘'],
        'price': [6000, 5000, 5000],
    },

    'popcorn1': [
        {'name': '치즈 팝콘', 'price': 6000},
        {'name': '카라멜 팝콘', 'price': 5000},
        {'name': '일반 팝콘', 'price': 5000},
    ],

}

print(f"{megaMovie['movie']}")
movieNumber = int(input("영화를 고르세요(0~2번) :"))
print(f"{megaMovie['popcorn']}")
popcornNumber = int(input("팝콘을 고르세요(0~2번) :"))

print(f"구매하신 영화는 {megaMovie['movie1'][movieNumber]['name']} 팝콘은 {megaMovie['popcorn1'][movieNumber]['name']}입니다.")
print(f"총 금액은 {megaMovie['movie1'][movieNumber]['price'] + megaMovie['popcorn1'][popcornNumber]['price']}")
