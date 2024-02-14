# 1.
# [표현식 for 항목 in 반복가능객체(리스트, 문자열, range, ...)
# [1 for i in range(100)
# a = [i for i in "chocolate"]
# b = [i+10 for i in [1,2,3]]


# # 2. 조건문 (filter 같은 느낌)
# [i for i in range(100)] # 짝수만 하고 싶다
# a = [i for i in range(100) if i % 2 == 0]
# print(a)
#
# # 10000까지 15의 배수
# b = [i for i in range(10001) if i % 15 == 0]
# print(b)

choList = ["Ghana", "Godiva", "hershey", "Royce"]  # 얘를 출력 [5,6,7,5]로 나타내 주세용
#
# # c = [choList for choList in range if choList]
# # print(c)
# # 답
# print([len(i) for i in choList])
#
# # 글자 개수가 짝수인 초콜렛만 나타내 주세요
# print([len(i)for i in choList] % 2 == 0) #타입이 맞지 않음 여쭤보기
# # 답
# print([i for i in choList if len(i) % 2 == 0])

# 알파벳 e가 들어가 있는 애들만 표현해주세요
# [i for i in choList [e]]
# 답
# [i for i in choList if 'e' in i]
# [i for i in choList if i.count('e') > 0]

# 3. 조건문(치환 느낌)
# a = [i if i % 2 == 0 else '🤍' for i in range(101)] #<<range가 정수형만 타겟인가?
# print(a)

# 4. 3의 배수이면 박수, 그게 아니면 그냥 나타내기
# b = [i if % 3 == 0 '👐' else for in in range(101)]

# b = ['👐' if i % 3 == 0 else i for i in range(101)]
# print(b)

# a 포함이면 초콜렛 아니면 문자 길이로 치환
# ['🍫' if i in 'a' else i for len(i) in range(101)] ## 문자랑 정수랑 타입이 안 맞아서 에러 뜨는 듯
# 답
# c = ['🍫'if 'a' in i else len(i) for i in choList]
# print(c)

# 369 게임
# 1~100까지 출력을 하는데, 3,6,9가 포함되어 있으면 '🙏'
# 아니면 그대로 출력 ex) 31 > 🙏, 33 > 🙏, 41 > 41

# d = ['🙏' if i % 3 == 0 else i for i in range(1,101)] # 맨 앞에 박수를 어떻게 없애는지 >>
# print(d)                                              # range()안의 범위를 (1,101)로 설정해 주면 된다

# 답
# e = ['🙏' if str(i % 10) in '369' or str(i // 10) in '369' else i for i in range(1, 101)]
# f = ['🙏' if '3' in str(i) or '6' in str(i) or '9' in str(i) else i for i in range(1, 101)]
# print(e)

# ctrl+a 전체선택 / ctrl+alt+l 예쁘게 정렬 / ctrl+w 커서 주위 부분 선택 (+ 후에 alt+j 누르면 해당 영역 한 번에 다 바꾸기 가능)/

# 4. 중첩 루프 컴프리헨션
# print([(i,j) for i in range(10) for j in range(10)])
# i 0 j 0 > i 0 j 1 > i 0 j 2 > ... > i 9 j 9 모든 경우의 수를 다 따지는 것

# 구구단 1단부터 9단까지 나오는 프로그램 만들기
# print([(i,j)for i in range(1,10) for j in range(1,10)])
#답
gugudan = ([f"{i}*{j} = {i*j}" for i in range(1,10) for j in range(1,10)])
print(gugudan)