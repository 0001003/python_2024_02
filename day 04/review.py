# 커피 리스트를 만들고
# 커피 4개를 임의로 넣고
# 유저에게 마시고 싶은 커피 번호를 선택하게 한 후
# ~~ 커피를 준비해 드리겠습니다. 하는 프로그램 만들기

coffee = ["아메리카노", "라떼", "자몽허니블랙티", "카페모카"]
num = int(input(f"{coffee}원하는 음료의 번호를 입력 : "))
print(f"{coffee[num-1]}를 준비해 드리겠습니다.")
