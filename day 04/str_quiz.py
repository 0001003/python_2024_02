# 1. 소문자로 된 문자열 입력 받고, 이를 모두 대문자로 변환하는 프로그램 만들기

# a=input("소문자로 된 문자열 입력 : ")
# "a".upper(a)
# print(a)

word = input("단어 입력 :")
up_word = word.upper()
print(up_word)


# 2. 노래 가사에서 단어 카운트

song = """Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Ever since the d-day y-you went away (no, I don't know how)
How to erase your body from out my brain (what you gon' do now?)
Maybe I should just focus on me instead (but all I think about)
Are the nights we were tangled up in your bed
Oh no (oh no)
Oh no (oh no)
You're goin' 'round in circles
Got you stuck up in my head, yeah
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Ever since the d-day y-you went away (someone tell me how)
How much more do I gotta drink for the pain (what you gon' do now?)
You did things to me that I just can't forget (now all I think about)
Are the nights we were tangled up in your bed
Oh no (oh no)
Oh no (oh no)
You're going 'round in circles
Got you stuck up in my head, yeah
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind (of my mind)
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Did you know you're the one that got away?
And even now, baby, I'm still not okay
Did you know that my dreams, they're all the same
Every time I close my eyes?
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
(Whoa)
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)"""

left = song.count("left")
right = song.count("right")
print(f"left: {left}, right: {right}")



# 3. 이메일 주소 분리 프로그램
# john.doe@example.com이 입력되면 john.doe와 example.com으로 분리


# a = input("이메일 주소 입력 :")


email = input("이메일 주소 : ")
result = email.split("@")
print(result)



