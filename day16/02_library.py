# 라이브러리 == 도구 모음집

import abc
import random       #난수
import math         #수학
import datetime     #날짜
import os           #폴더, 경로[#ios, window, linux, mac, android] = os

# a = datetime.datetime.now()
# b = a.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
# print(b)

# 바탕화면 경로를 변수에 넣기
path = os.path.join(os.environ['USERPROFILE'],'Desktop')
# '요즘 경제 쉽지 않다.' 폴더의 경로 만들기
new_path = os.path.join(path, '요즘 경제 쉽지 않다.') # 바탕화면에 폴더가 요즘 경제 쉽지 않다 라는 폴더가 생김.
# 폴더 만들기 (new_path에다가)
os.makedirs(new_path)
